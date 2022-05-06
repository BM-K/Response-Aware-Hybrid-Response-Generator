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
|Q-RQ<sup>'</sup>-R<sup>'</sup>-Sim<sup>†</sup>|**36.32**|***62.83*|**21.41**|

### Business
|Model|BLEU-1|BLEU-2|BLEU-3|BLEU-4|Dist-1|Dist-2|Entropy|
|:----------:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|Base|27.68|11.67|6.37|3.96|35.14|74.22|10.24|
|QSim|28.09|12.22|6.65|4.11|**38.39**|**78.83**|**10.35**|
|RSim|28.37|12.89|7.34|4.78|37.94|77.91|10.32|
|QRSim<sup>†</sup>|**28.76**|**13.24**|**7.61**|**4.86**|38.1|78.72|10.29|

## ToDo
- [ ] Multi-Turn
- [ ] Knowledge-Base
