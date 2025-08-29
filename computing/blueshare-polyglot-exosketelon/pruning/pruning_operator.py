# File: bpets/core/dimension_control/pruning/pruning_operator.py
"""4D Tensor Pruning Operator for BPETS Dimension Control"""

import numpy as np
from typing import Tuple

H_CRIT = 1.0  # configurable

def node_pruning(tensor: np.ndarray, 
                 w: np.ndarray, 
                 tau: float) -> Tuple[np.ndarray, float]:
    """Apply node pruning to 4D tensor based on weight threshold.
    
    Args:
        tensor: Input 4D tensor (T×S×F×C)
        w: Weight vector for feature dimension
        tau: Pruning threshold
    
    Returns:
        Pruned tensor and normalized Hamiltonian energy
    """
    mask = w >= tau
    # Broadcast mask across all dimensions except feature axis
    mask_4d = mask[np.newaxis, np.newaxis, :, np.newaxis]
    pruned = tensor * mask_4d
    H_norm = min(1.0, w.sum() / H_CRIT)
    return pruned, H_norm

def edge_cluster_pruning(adj: np.ndarray,
                        cluster: np.ndarray,
                        w: np.ndarray,
                        tau: float) -> np.ndarray:
    """Prune edges while preserving intra-cluster connectivity.
    
    Args:
        adj: Adjacency matrix (F×F)
        cluster: Cluster assignment vector
        w: Edge weight matrix
        tau: Pruning threshold
    
    Returns:
        Pruned adjacency matrix
    """
    # Keep edges above threshold OR within same cluster
    mask = (w >= tau) | (cluster[:, None] == cluster[None, :])
    return adj * mask

def compute_fod_score(pruned_tensor: np.ndarray, 
                     H_norm: float) -> float:
    """Compute Freedom of Dexterity score from pruned tensor."""
    # Flatten to 2D for rank computation
    reshaped = pruned_tensor.reshape(-1, pruned_tensor.shape[-1])
    _, s, _ = np.linalg.svd(reshaped, full_matrices=False)
    rank_eff = np.sum(s > 1e-10)  # numerical rank
    fod = 6 * (rank_eff / 6) * (1 - H_norm)
    return np.clip(fod, 0, 6)
