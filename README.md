# Street2Shop implementation with keras

## Task
Clothing image retrieval from consumer(street) image to shop(online) image.

### Goal
Compare Models for clothing retrieval.
Main: VGG16 + Triplet Loss/Improved Triplet Loss
1. SingleNetwork for one input
2. DualNetwork for one input

## Implementation
These notebooks are implemented by python3.5 or 3.6, keras 2.2.1. Sorry, I use Japanese for comment in my notebook, haha.
Please execute this command for building my environment.
```shell
$ conda env create -n {new environment name} -f env_zkk.yml
```
## Dataset
I used `DeepFashion` Dataset to train and test my model.
- anchor = street image
- positive = shop image consistent to anchor
- negative = shop image not consistent to anchor

###  data example
![](./readme_imgs/tripletSample.png)

## Reference
- DeepFashion(https://liuziwei7.github.io/projects/DeepFashion.html)