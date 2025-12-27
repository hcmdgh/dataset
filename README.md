# 简介

收集一些图神经网络、推荐系统等领域的公开的数据集，以及相应的预处理代码。

# 数据集描述

- 异质图
    - [ACM](https://huggingface.co/datasets/genghaobuaa/ACM)
    - [DBLP](https://huggingface.co/datasets/genghaobuaa/DBLP)
    - [IMDB](https://huggingface.co/datasets/genghaobuaa/IMDB)
- 图集合
    - [TRIANGLES](https://huggingface.co/datasets/genghaobuaa/TRIANGLES)
    - [substructure_counting](https://huggingface.co/datasets/genghaobuaa/substructure_counting)
    - [EXP](https://huggingface.co/datasets/genghaobuaa/EXP)

# 使用方式

## 完整下载

```bash
git lfs install
git clone https://github.com/hcmdgh/dataset --recursive
```

## 按需下载

```bash
git lfs install
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/hcmdgh/dataset --recursive

# 进入某个数据集目录
git lfs pull 
```

## 加载数据集

通过各个数据集目录下的load.py，加载数据集。

# 原始数据下载

数据集的原始数据存储在[我的Hugging Face空间](https://huggingface.co/genghaobuaa/datasets)。
