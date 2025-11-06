import numpy as np
from esm_seu import ESMSEU

model = ESMSEU(alpha=0.6, eta=1.0, beta=2.0, lam=0.05)

# Simulasi data
grad_loss = np.random.normal(0, 1, 100)
delta_h = np.random.normal(0, 0.2, 100)
p = np.abs(np.random.dirichlet(np.ones(5)))
dp_dt = np.gradient(p)

phi_val = model.phi(grad_loss, delta_h, p, dp_dt)
print(f"Unified ESM–SEU Value: {phi_val:.4f}")
