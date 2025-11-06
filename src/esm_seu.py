import numpy as np

class ESMSEU:
    def __init__(self, alpha=0.5, eta=1.0, beta=1.0, lam=0.1):
        self.alpha = alpha
        self.eta = eta
        self.beta = beta
        self.lam = lam

    def esm(self, grad_loss, delta_h):
        """Empirical Stability Metric (ESM)"""
        weight = 1 / (1 + np.exp(-self.beta * delta_h))
        return np.mean(np.square(grad_loss) / weight)

    def seu(self, p, dp_dt):
        """Structural Entropy Utility (SEU)"""
        p = np.clip(p, 1e-12, 1.0)  # prevent log(0)
        entropy = -np.sum(p * np.log(p))
        var_term = self.lam * np.var(dp_dt)
        return entropy + var_term

    def phi(self, grad_loss, delta_h, p, dp_dt):
        """Unified ESM–SEU functional"""
        esm_val = self.esm(grad_loss, delta_h)
        seu_val = self.seu(p, dp_dt)
        return self.alpha * esm_val + (1 - self.alpha) * seu_val
