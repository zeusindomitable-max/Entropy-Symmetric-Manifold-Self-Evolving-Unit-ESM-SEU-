import numpy as np

class EmpiricalStabilityMetric:
    """
    ESM quantifies effective energy dissipation under logistic modulation.
    """

    def __init__(self, beta: float = 1.0):
        self.beta = beta

    def compute(self, grad_loss, delta_H):
        grad_sq = np.sum(np.square(grad_loss))
        denom = 1 + np.exp(-self.beta * delta_H)
        return grad_sq / denom


class StructuralEntropyUtility:
    """
    SEU measures entropy regularization with dynamic penalty.
    """

    def __init__(self, lam: float = 1.0):
        self.lam = lam

    def compute(self, p, dp_dt):
        entropy = -np.sum(p * np.log(np.clip(p, 1e-10, 1.0)))
        variance = np.var(dp_dt)
        return entropy + self.lam * variance


class UnifiedESMSEU:
    """
    Combine ESM and SEU into unified functional Φ_ESM-SEU
    """

    def __init__(self, alpha=0.5, beta=1.0, lam=1.0):
        self.alpha = alpha
        self.esm = EmpiricalStabilityMetric(beta)
        self.seu = StructuralEntropyUtility(lam)

    def compute(self, grad_loss, delta_H, p, dp_dt):
        esm_val = self.esm.compute(grad_loss, delta_H)
        seu_val = self.seu.compute(p, dp_dt)
        return self.alpha * esm_val + (1 - self.alpha) * seu_val
