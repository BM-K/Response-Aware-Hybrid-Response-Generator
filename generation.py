import csv
import time
import torch
from utils import *
from random import *
from tqdm import tqdm
from sklearn.metrics.pairwise import paired_cosine_distances


class DialogueGeneration():

    def __init__(self, 
                 args=None,
                 retrieval_model=None,
                 generative_model=None,
                 retrieval_tokenizer=None,
                 generative_tokenizer=None,
                 embedded_database=None,
                 corpus=None,
                 faiss_index=None,
        ):

        self.args = args
        
        self.retrieval_model = retrieval_model
        self.generative_model = generative_model

        self.retrieval_tokenizer = retrieval_tokenizer
        self.generative_tokenizer = generative_tokenizer

        self.embedded_database = embedded_database
        self.corpus = corpus

        self.faiss_index = faiss_index
        
        self.pad_idx = generative_tokenizer.convert_tokens_to_ids(generative_tokenizer.pad_token)
        self.eos_idx = generative_tokenizer.convert_tokens_to_ids(generative_tokenizer.eos_token)
        self.sep_idx = generative_tokenizer.convert_tokens_to_ids(generative_tokenizer.sep_token)
    
    def api_inference(self,
        utterance: str = None,
        ):
    
        result = {
                "retriever": list(),
                "generator": list()
                 }
        generative_model_inputs = []

        with torch.no_grad():
            utter = utterance
            
            tokenized_input = self.retrieval_tokenizer(utter.strip(),
                                                       truncation=True,
                                                       return_tensors="pt",
                                                       max_length=self.args.max_len,
                                                       padding='max_length')
            tokenized_input.to(self.args.device)
            
            embedded_input, _ = self.retrieval_model(tokenized_input, response=True)
            embedded_input = embedded_input[:, :1]
            
            if self.args.mips == 'False':
                _, I = self.faiss_index.search(embedded_input.squeeze(0).cpu().detach().numpy(), self.args.num_ks)
                preds = torch.tensor(I).squeeze(0)
            else:
                logits = torch.matmul(embedded_input.squeeze(0),
                                      self.embedded_database.to(self.args.device).transpose(-1, -2))
                preds = logits.topk(k=self.args.num_ks, dim=-1)[-1].squeeze(0)
                
            inputs = self.generative_tokenizer.encode(utter) + [self.sep_idx]
    
            print(f'\n\nUser: {utterance}\n')
            print("-----검색결과-----")
            for step, idx in enumerate(preds):
                proactive_response = self.generative_tokenizer.encode(self.corpus[idx].split('[SEP]')[-1])
                result["retriever"].append({
                    f"answer {step+1}": self.corpus[idx].split('[SEP]')[-1],
                })
                print(f"{step+1}.{self.corpus[idx].split('[SEP]')[-1]}")
                input_ = add_padding_data(inputs + proactive_response,
                                          self.args.max_len,
                                          self.pad_idx,
                                          self.eos_idx)
                generative_model_inputs.append(input_)
            print("------------------\n")
            
            input_list = torch.LongTensor(generative_model_inputs).to(self.args.device).unsqueeze(0)
            outputs = self.generative_model(input_list)

            hyp = self.generative_tokenizer.decode(outputs.squeeze(0), skip_special_tokens=True)
            print(f'Bot: {hyp}\n')

            result["generator"].append({
                f"Bot response": hyp
            })

            return result
