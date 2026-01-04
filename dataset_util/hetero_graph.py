import torch 
import torch_geometric.utils as pyg_util 
from torch_geometric.data import Data, HeteroData
import pickle 
import os 

dataset_root = "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-hmart-waimaiad/canyin/genghao07/dataset/hetero_graph"


def load_rcdd_subgraph_dataset(
    val_ratio: float = 0.1,
) -> HeteroData:
    dataset_dir = os.path.join(dataset_root, 'RCDD')

    with open(os.path.join(dataset_dir, 'processed_data/subgraph.pkl'), 'rb') as r:
        graph = pickle.load(r)

    train_val_mask_1d = graph['item'].train_mask
    train_val_idx_1d = train_val_mask_1d.nonzero().flatten()
    train_val_cnt = len(train_val_idx_1d)
    val_cnt = int(train_val_cnt * val_ratio) 
    train_cnt = train_val_cnt - val_cnt
    assert train_cnt > 0 and val_cnt > 0

    generator = torch.Generator().manual_seed(42)
    perm_1d = torch.randperm(train_val_cnt, generator=generator)
    train_idx_1d = train_val_idx_1d[perm_1d[:train_cnt]]
    val_idx_1d = train_val_idx_1d[perm_1d[train_cnt:]]
    train_mask_1d = torch.zeros_like(train_val_mask_1d)
    train_mask_1d[train_idx_1d] = True
    val_mask_1d = torch.zeros_like(train_val_mask_1d)
    val_mask_1d[val_idx_1d] = True 

    graph['item'].train_mask = train_mask_1d
    graph['item'].val_mask = val_mask_1d

    return graph 


def load_heco_acm_dataset(
    split: int,
) -> HeteroData:
    graph_path = os.path.join(dataset_root, 'HeCo/ACM/processed_data/graph.pkl')
    split_path = os.path.join(dataset_root, 'HeCo/ACM/processed_data/split.pkl')

    with open(graph_path, 'rb') as r:
        graph = pickle.load(r)

    with open(split_path, 'rb') as r:
        train_mask_dict, val_mask_dict, test_mask_dict = pickle.load(r)

    graph['paper']['train_mask'] = train_mask_dict[split]
    graph['paper']['val_mask'] = val_mask_dict[split]
    graph['paper']['test_mask'] = test_mask_dict[split]

    return graph 


def load_heco_dblp_dataset(
    split: int,
) -> HeteroData:
    graph_path = os.path.join(dataset_root, 'HeCo/DBLP/processed_data/graph.pkl')
    split_path = os.path.join(dataset_root, 'HeCo/DBLP/processed_data/split.pkl')

    with open(graph_path, 'rb') as r:
        graph = pickle.load(r)

    with open(split_path, 'rb') as r:
        train_mask_dict, val_mask_dict, test_mask_dict = pickle.load(r)

    graph['author']['train_mask'] = train_mask_dict[split]
    graph['author']['val_mask'] = val_mask_dict[split]
    graph['author']['test_mask'] = test_mask_dict[split]

    return graph 


def load_heco_aminer_dataset(
    split: int,
    add_node_feat: str,
) -> HeteroData:
    graph_path = os.path.join(dataset_root, 'HeCo/AMiner/processed_data/graph.pkl')
    split_path = os.path.join(dataset_root, 'HeCo/AMiner/processed_data/split.pkl')

    with open(graph_path, 'rb') as r:
        graph = pickle.load(r)

    with open(split_path, 'rb') as r:
        train_mask_dict, val_mask_dict, test_mask_dict = pickle.load(r)

    graph['paper']['train_mask'] = train_mask_dict[split]
    graph['paper']['val_mask'] = val_mask_dict[split]
    graph['paper']['test_mask'] = test_mask_dict[split]

    if add_node_feat == 'onehot':
        pass 
    elif add_node_feat.startswith('randn_'):
        node_feat_dim = int(add_node_feat.removeprefix('randn_'))

        for node_type in graph.node_types:
            node_feat = torch.randn(int(graph[node_type].num_nodes), node_feat_dim, dtype=torch.float32)
            graph[node_type].x = node_feat
    else:
        raise ValueError 

    return graph 


def load_heco_freebase_dataset(
    split: int,
    add_node_feat: str,
) -> HeteroData:
    graph_path = os.path.join(dataset_root, 'HeCo/Freebase/processed_data/graph.pkl')
    split_path = os.path.join(dataset_root, 'HeCo/Freebase/processed_data/split.pkl')

    with open(graph_path, 'rb') as r:
        graph = pickle.load(r)

    with open(split_path, 'rb') as r:
        train_mask_dict, val_mask_dict, test_mask_dict = pickle.load(r)

    graph['movie']['train_mask'] = train_mask_dict[split]
    graph['movie']['val_mask'] = val_mask_dict[split]
    graph['movie']['test_mask'] = test_mask_dict[split]

    if add_node_feat == 'onehot':
        pass 
    elif add_node_feat.startswith('randn_'):
        node_feat_dim = int(add_node_feat.removeprefix('randn_'))

        for node_type in graph.node_types:
            node_feat = torch.randn(int(graph[node_type].num_nodes), node_feat_dim, dtype=torch.float32)
            graph[node_type].x = node_feat
    else:
        raise ValueError 

    return graph 


def load_hin_aminer_dataset(
    split: int,
    add_node_feat: str,
) -> HeteroData:
    graph_path = os.path.join(dataset_root, 'HIN-Dataset/processed_data/graph.pkl')
    split_path = os.path.join(dataset_root, 'HIN-Dataset/processed_data/split.pkl')

    with open(graph_path, 'rb') as r:
        graph = pickle.load(r)

    with open(split_path, 'rb') as r:
        train_mask_dict, val_mask_dict, test_mask_dict = pickle.load(r)

    graph['paper']['train_mask'] = train_mask_dict[split]
    graph['paper']['val_mask'] = val_mask_dict[split]
    graph['paper']['test_mask'] = test_mask_dict[split]

    if add_node_feat == 'onehot':
        for node_type in graph.node_types:
            num_nodes = int(graph[node_type].num_nodes)

            node_feat = torch.sparse_coo_tensor(
                indices = torch.arange(num_nodes).reshape(1, num_nodes).repeat(2, 1),
                values = torch.ones(num_nodes, dtype=torch.float32),
                size = (num_nodes, num_nodes),
            )
            graph[node_type].x = node_feat
    elif add_node_feat.startswith('randn_'):
        node_feat_dim = int(add_node_feat.removeprefix('randn_'))

        for node_type in graph.node_types:
            num_nodes = int(graph[node_type].num_nodes)
            node_feat = torch.randn(num_nodes, node_feat_dim, dtype=torch.float32)
            graph[node_type].x = node_feat
    else:
        raise ValueError 

    return graph 


def load_imdb_dataset(
    split: str | int,
) -> HeteroData:
    graph_path = os.path.join(dataset_root, 'IMDB/processed_data/graph.pkl')
    split_path = os.path.join(dataset_root, 'IMDB/processed_data/split.pkl')

    with open(graph_path, 'rb') as r:
        graph = pickle.load(r)

    if split == 'official':
        pass 
    else:
        split = int(split)

        with open(split_path, 'rb') as r:
            train_mask_dict, val_mask_dict, test_mask_dict = pickle.load(r)

        graph['movie']['train_mask'] = train_mask_dict[split]
        graph['movie']['val_mask'] = val_mask_dict[split]
        graph['movie']['test_mask'] = test_mask_dict[split]

    return graph 


if __name__ == '__main__':
    dataset = load_imdb_dataset(split=20)
    print(dataset)
