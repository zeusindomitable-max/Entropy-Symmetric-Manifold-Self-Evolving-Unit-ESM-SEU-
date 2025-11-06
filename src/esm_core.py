import numpy as np

class EffectiveHamiltonian:
    """
    Core definition for effective Hamiltonian mapping.
    H_eff = η * L
    """

    def __init__(self, eta: float = 1.0):
        self.eta = eta

    def compute(self, loss_value: float) -> float:
        """Compute effective Hamiltonian."""
        return self.eta * loss_value

    def delta(self, loss_diff: float) -> float:
        """Compute ΔH_eff from ΔL."""
        return self.eta * loss_diff
      
