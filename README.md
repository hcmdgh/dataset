# 简介

收集一些图神经网络、推荐系统等领域的公开的数据集，以及相应的预处理代码。

# 数据集描述

- 异质图
    - [ACM (from HeCo)](https://huggingface.co/datasets/genghaobuaa/HeCo)
    - [DBLP (from HeCo)](https://huggingface.co/datasets/genghaobuaa/HeCo)
    - [Freebase (from HeCo)](https://huggingface.co/datasets/genghaobuaa/HeCo)
    - [AMiner (from HeCo)](https://huggingface.co/datasets/genghaobuaa/HeCo)
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

通过dataset_util，加载相应的数据集：

```python
import dataset_util

dataset = load_acm_dataset(split=20)
print(dataset)
```

# 原始数据下载

数据集的原始数据存储于：[https://huggingface.co/genghaobuaa/datasets](https://huggingface.co/genghaobuaa/datasets)
