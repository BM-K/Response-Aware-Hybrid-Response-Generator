# Knowledge-Augmented-Dialogue-Generation

## Overall Architecture
 <img src=https://user-images.githubusercontent.com/55969260/161927957-3f4192a3-ac0d-4df3-8517-2d45f15f5b13.png>

## Datasets
| Datasets                  | Training | Validation | Testing |
|----------|:----:|:----:|:----:|
| AI-Hub(SBusiness) | 656,332 | 28,361 | 28,464 |

## Results
### Retrieval Model
|Model|Hit@10|Hit@100|MRR@100|
|:----------:|:----:|:----:|:----:|
|Q-R<sup>'</sup>|17.43|37.31|9.28|
|Q-Q<sup>'</sup>|27.51|51.56|16.53|
|QR<sup>\*</sup>-Q<sup>'</sup>R<sup>'</sup>|**36.32**|**62.83**|**21.41**|

### Business
|Model|BLEU-1|BLEU-2|BLEU-3|BLEU-4|Dist-1|Dist-2|
|:----------:|:----:|:----:|:----:|:----:|:----:|:----:|
|NoRet|18.48|12.41|8.65|6.19|1.04|17.41|
|Q-R<sup>'</sup>|18.27|12.15|8.31|5.79|1.10|20.36|
|Q-Q<sup>'</sup>|18.52|12.37|8.52|6.01|1.11|20.28|
|QR<sup>*</sup>-Q<sup>'</sup>R<sup>'</sup>|19.96|13.72|9.84|7.31|1.16|22.12|

### Latency
|                  | FAISS | MIPS |
|----------|:----:|:----:|
| Latency | 0.127s | 0.474s |
`NOTE`: FAISS Centroid 64

## ToDo
- [ ] Multi-Turn
- [ ] Knowledge-Base
