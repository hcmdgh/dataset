import torch 
from torch_geometric.data import Data, Batch 
from torch_geometric.utils import add_remaining_self_loops 
import pickle 
import os 

dataset_root = "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-hmart-waimaiad/canyin/genghao07/dataset/graph_collection"


def transform_graph_batch(
    graph_batch: Batch,
    add_node_feat: str,
    add_self_loop: bool,
) -> Batch:
    graph_list = graph_batch.to_data_list()

    for graph in graph_list:
        if add_self_loop:
            graph.edge_index, _ = add_remaining_self_loops(
                edge_index = graph.edge_index, 
                num_nodes = int(graph.num_nodes),
            )

        if add_node_feat == 'none':
            pass
        elif add_node_feat == 'ones':
            graph.x = torch.ones(int(graph.num_nodes), 1, dtype=torch.float32)
        elif add_node_feat.startswith('randn_'):
            node_feat_dim = int(add_node_feat.removeprefix('randn_')) 
            graph.x = torch.randn(int(graph.num_nodes), node_feat_dim, dtype=torch.float32)
        else:
            raise ValueError 
        
    graph_batch = Batch.from_data_list(graph_list)

    return graph_batch 


def load_triangles_dataset(
    add_node_feat: str,
    add_self_loop: bool,
) -> tuple[Batch, Batch, Batch]:
    dataset_dir = os.path.join(dataset_root, 'TRIANGLES')
    graph_batch_list = [] 

    for split in ['train', 'val', 'test']:
        with open(os.path.join(dataset_dir, f'processed_data/{split}_graph_batch.pkl'), 'rb') as r:
            graph_batch = pickle.load(r)

        graph_batch = transform_graph_batch(
            graph_batch = graph_batch,
            add_node_feat = add_node_feat,
            add_self_loop = add_self_loop,
        )

        graph_batch_list.append(graph_batch)
    
    return tuple(graph_batch_list)


def load_substructure_counting_dataset(
    add_node_feat: str,
    add_self_loop: bool,
) -> tuple[Batch, Batch, Batch]:
    dataset_dir = os.path.join(dataset_root, 'substructure_counting')
    graph_batch_list = [] 

    for split in ['train', 'val', 'test']:
        with open(os.path.join(dataset_dir, f'processed_data/{split}_graph_batch.pkl'), 'rb') as r:
            graph_batch = pickle.load(r)

        graph_batch = transform_graph_batch(
            graph_batch = graph_batch,
            add_node_feat = add_node_feat,
            add_self_loop = add_self_loop,
        )

        graph_batch_list.append(graph_batch)
    
    return tuple(graph_batch_list)


def load_exp_dataset(
    add_node_feat: str,
    add_self_loop: bool,
) -> Batch:
    dataset_dir = os.path.join(dataset_root, 'EXP')

    with open(os.path.join(dataset_dir, f'processed_data/graph_batch.pkl'), 'rb') as r:
        graph_batch = pickle.load(r)

    graph_batch = transform_graph_batch(
        graph_batch = graph_batch,
        add_node_feat = add_node_feat,
        add_self_loop = add_self_loop,
    )

    return graph_batch


if __name__ == '__main__':
    data = load_exp_dataset(
        add_node_feat = 'randn_128',
        add_self_loop = True,
    )
    print(data)
