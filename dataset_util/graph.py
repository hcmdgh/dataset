import torch 
from torch_geometric.data import Data, Batch 
from torch_geometric.utils import add_remaining_self_loops 
import pickle 
import os 

dataset_root = "/mnt/dolphinfs/hdd_pool/docker/user/hadoop-hmart-waimaiad/canyin/genghao07/dataset/graph"


def load_ours_triangle_identification_dataset(
    add_node_feat: str,
    add_self_loop: bool,
) -> Data:
    dataset_dir = os.path.join(dataset_root, 'ours_triangle_identification')

    with open(os.path.join(dataset_dir, f'processed_data/graph.pkl'), 'rb') as r:
        graph = pickle.load(r)

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

    return graph 


if __name__ == '__main__':
    data = load_ours_triangle_identification_dataset(
        add_node_feat = 'randn_128',
        add_self_loop = True,
    )
    print(data)
