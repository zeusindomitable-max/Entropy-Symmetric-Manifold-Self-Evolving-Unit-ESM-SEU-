import numpy as np

def entropy_symmetric_metric(S, delta_t=1e-3):
    """
    Approximate Entropy Symmetric Metric (ESM)
    ------------------------------------------
    dS/dt + ∇S * symmetry_correction
    """
    dS_dt = np.gradient(S) / delta_t
    grad_S = np.gradient(S)
    return dS_dt + grad_S ** 2
