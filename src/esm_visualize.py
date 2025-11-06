import matplotlib.pyplot as plt

def plot_entropy(S):
    plt.plot(S, color='blue', label='Entropy (S)')
    plt.title('Entropy Symmetric Metric Simulation')
    plt.legend()
    plt.show()
