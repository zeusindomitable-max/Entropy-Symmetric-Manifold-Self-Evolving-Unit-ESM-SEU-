import numpy as np
from .esm_seu import esm_stability_energy
from .esm_core import entropy_symmetric_metric

def simulate_entropy_system(size=1000):
    S = np.sin(np.linspace(0, 10, size)) ** 2
    esm_val = entropy_symmetric_metric(S)
    seu_val = esm_stability_energy(np.mean(np.abs(np.gradient(S))), np.mean(esm_val))
    return seu_val, S
  
