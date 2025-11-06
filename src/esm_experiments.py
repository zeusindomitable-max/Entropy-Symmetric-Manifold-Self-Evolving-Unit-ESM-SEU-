import numpy as np
from .esm_core import EffectiveHamiltonian
from .esm_seu import UnifiedESMSEU

def synthetic_experiment():
    """
    Simple test simulation to verify the ESM–SEU behavior.
    """

    np.random.seed(42)

    # Simulate losses
    losses = np.linspace(1.0, 0.1, 50)
    grad_loss = np.gradient(losses)
    delta_L = np.gradient(losses)

    # Probability evolution
    p = np.abs(np.random.rand(50))
    p /= np.sum(p)
    dp_dt = np.gradient(p)

    # Initialize models
    H_eff = EffectiveHamiltonian(eta=0.7)
    unified = UnifiedESMSEU(alpha=0.6, beta=1.2, lam=0.5)

    # Compute unified metric
    phi_vals = []
    for i in range(len(losses)):
        delta_H = H_eff.delta(delta_L[i])
        phi = unified.compute(grad_loss, delta_H, p, dp_dt)
        phi_vals.append(phi)

    return np.array(phi_vals)
  
