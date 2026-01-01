import torch 
from torch import Tensor 
from torch_geometric.data import Data, Batch 
import json 
import pickle 
import os 
from dataclasses import dataclass

dataset_root = "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-hmart-waimaiad/canyin/genghao07/dataset/recommendation"


@dataclass 
class MovieLens10MDataset:
    graph: Data 
    train_pos_edge_index: Tensor 
    train_neg_edge_index: Tensor 
    val_pos_edge_index: Tensor 
    val_neg_edge_index: Tensor
    test_pos_edge_index: Tensor 
    test_neg_edge_index: Tensor

    def __init__(self):
        dataset_dir = os.path.join(dataset_root, 'MovieLens/MovieLens-10M/preprocess_ctr_graph/data')

        with open(os.path.join(dataset_dir, 'graph.pkl'), 'rb') as r:
            graph = pickle.load(r)

        with open(os.path.join(dataset_dir, 'train_pos_edge_index.pkl'), 'rb') as r:
            train_pos_edge_index = pickle.load(r)

        with open(os.path.join(dataset_dir, 'train_neg_edge_index.pkl'), 'rb') as r:
            train_neg_edge_index = pickle.load(r)

        with open(os.path.join(dataset_dir, 'val_pos_edge_index.pkl'), 'rb') as r:
            val_pos_edge_index = pickle.load(r)

        with open(os.path.join(dataset_dir, 'val_neg_edge_index.pkl'), 'rb') as r:
            val_neg_edge_index = pickle.load(r)

        with open(os.path.join(dataset_dir, 'test_pos_edge_index.pkl'), 'rb') as r:
            test_pos_edge_index = pickle.load(r)

        with open(os.path.join(dataset_dir, 'test_neg_edge_index.pkl'), 'rb') as r:
            test_neg_edge_index = pickle.load(r)

        self.graph = graph
        self.train_pos_edge_index = train_pos_edge_index
        self.train_neg_edge_index = train_neg_edge_index
        self.val_pos_edge_index = val_pos_edge_index
        self.val_neg_edge_index = val_neg_edge_index
        self.test_pos_edge_index = test_pos_edge_index
        self.test_neg_edge_index = test_neg_edge_index


if __name__ == '__main__':
    data = MovieLens10MDataset()
    print(data)
