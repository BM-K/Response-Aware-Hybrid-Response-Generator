import uvicorn
import configparser
from typing import Optional
from pydantic import BaseModel

from database import Database
from setting import Arguments, Setting
from generation import DialogueGeneration
from fastapi import Body, FastAPI, APIRouter, UploadFile

router = APIRouter(prefix = '/api/v1')


app = FastAPI(
    title = "KB Single-Turn Chitchat Server API",
    version = "0.0.1"
)

def init(args):
    
    retrieval_model, generative_model, retrieval_tokenizer, generative_tokenizer = Setting(args).model()
    embedded_database, corpus, faiss_index = Database(args).offline_embedding(retrieval_model, retrieval_tokenizer)
    
    dg = DialogueGeneration(args=args,
                            retrieval_model=retrieval_model,
                            generative_model=generative_model,
                            retrieval_tokenizer=retrieval_tokenizer,
                            generative_tokenizer=generative_tokenizer,
                            embedded_database=embedded_database,
                            corpus=corpus,
                            faiss_index=faiss_index,)

    return dg


class Inference(BaseModel):
    utterance: str
    generate_error : Optional[bool] = False

# Inference
@router.post('/')
async def inference_start(Inference: Inference):

    utterance = Inference.utterance

    try:
        result = dg.api_inference(utterance)

        return {'code': 1, 'result' : result, 'message': 'Retriever KB chitchat (without KB) successful!'}
    except:
        return {'code': 0, 'message': 'Retriever KB chitchat (without KB) failed!'}

app.include_router(router)

if __name__ == '__main__':
    args = Arguments().run()
    dg = init(args)
    uvicorn.run(app, host = "0.0.0.0", port = int(7000))
