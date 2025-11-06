import matplotlib.pyplot as plt
from .esm_experiments import synthetic_experiment

def plot_experiment_results():
    phi_vals = synthetic_experiment()
    plt.figure(figsize=(7, 4))
    plt.plot(phi_vals, label="Φ_ESM–SEU", linewidth=2)
    plt.xlabel("Iteration")
    plt.ylabel("Unified Stability Metric")
    plt.title("Empirical Stability Evolution")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
