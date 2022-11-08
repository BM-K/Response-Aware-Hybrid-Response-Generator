# Response-Aware-Hybrid-Response-Generator


## Overall Architecture

## Datasets
| Datasets                  | Training | Validation | Testing |
|----------|:----:|:----:|:----:|
| AI-Hub | 656,332 | 28,361 | 28,464 |

## Results
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

### Latency
|                  | FAISS | MIPS |
|----------|:----:|:----:|
| Latency | 0.127s | 0.474s |

`NOTE`: FAISS Centroid 64
