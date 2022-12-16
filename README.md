# Response-Aware-Hybrid-Response-Generator
Only for inference

## Overall Architecture
> **Note** <br>
> Not published yet

## Datasets
| Datasets                  | Training | Validation | Testing |
|----------|:----:|:----:|:----:|
| AI-Hub | 656,332 | 28,361 | 28,464 |

## Results of AI-Hub Dataset
### Retrieval Model
|Model|Hit@10|Hit@100|MRR@10|MRR@100|
|:----------:|:----:|:----:|:----:|:----:|
|Q-CanAns|14.80|29.29|7.56|8.13|
|Q-CanQue|28.03|46.61|16.15|16.53|
|QR<sup>\'</sup>-CanQueAns|**36.61**|**55.28**|**19.50**|**21.41**|

### Hybrid Response Generator
|Model|BLEU-1|BLEU-2|BLEU-3|BLEU-4|Dist-1|Dist-2|
|:----------:|:----:|:----:|:----:|:----:|:----:|:----:|
|NoRet|18.48|12.41|8.65|6.19|1.04|17.41|
|Q-CanAns|18.32|12.16|8.31|5.81|1.10|20.17|
|Q-CanQue|18.61|12.47|8.63|6.12|1.11|20.56|
|QR<sup>\'</sup>-CanQueAns|**19.96**|**13.72**|**9.84**|**7.31**|**1.16**|**22.12**|

## API Inference
```
pip install -r requirements.txt
```
```
CUDA_VISIBLE_DEVICES=1 python main.py \
  --lang ko \
  --model hybrid \
  --corpus_v1 data/database_v1.tsv \
  --corpus_v2 data/database_v2.tsv \
  --retrieval_ckpt models/outputs/single_retrieval_model.pt \
  --generative_ckpt models/outputs/single_generative_model.pt \
  --retrieval_mode base \
  --num_centroids 64 \
  --n_beams 5 \
  --min_length 3 \
  --db_embedding_bsz 256 \
  --num_ks 3 \
  --max_len 80 
```
<details>
<summary>Hyperparameters</summary>
<div markdown="1">

> - end_command: user inference시 대화 중단을 위한 command key <br>
> - num_ks: 사용할 retrieved response 개수
> - ret_max_len: 검색시 최대 token 개수
> - mips: True는 maximum inner product 계산, False는 FAISS Lib 사용
> - num_centroids: FAISS centroids 개수
> - n_beams: 디코딩시 beam 개수
> - min_length: 디코딩시 출력 최소 token 개수
> - retrieval_ckpt: 검색 모델 checkpoint 위치
> - generative_ckpt: 생성 모델 checkpoint 위치

</div>
</details>

## Demo with FastAPI
<img src = "https://user-images.githubusercontent.com/55969260/200460525-ac04b760-0b66-4371-84f5-d82f15d1b1e6.gif"> <br>
