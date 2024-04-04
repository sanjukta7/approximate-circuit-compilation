import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

# Define the MRF structure
num_nodes = 100  # Number of nodes in the MRF
edges = [(i, j) for i in range(num_nodes) for j in range(i+1, num_nodes)]  # All possible edges

# Define the potential functions
def node_potential(x):
    x = np.clip(x, -10, 10)  # Clip values to avoid overflow
    return np.exp(-0.5 * np.sum(x**2))  # Gaussian prior

def edge_potential(x1, x2):
    x1 = np.clip(x1, -10, 10)  # Clip values to avoid overflow
    x2 = np.clip(x2, -10, 10)  # Clip values to avoid overflow
    diff = x1 - x2
    diff = np.clip(diff, -10, 10)  # Clip difference to avoid overflow
    return np.exp(-0.5 * diff**2)  # Gaussian edge potential

# Noise addition process
def add_noise(x, sigma):
    return x + np.random.randn(*x.shape) * sigma

# Noise removal process
def remove_noise(x, sigma):
    # Initialize the belief propagation messages
    messages = {edge: np.zeros(x.shape) for edge in edges}

    for iteration in range(10):  # Perform belief propagation iterations
        for edge in edges:
            i, j = edge
            product = node_potential(x[i]) * node_potential(x[j])
            messages[edge] = 1.0 / sigma**2 * (x[i] - x[j])
            for k in range(num_nodes):
                if k != i and k != j:
                    product *= edge_potential(x[i], x[k]) * edge_potential(x[j], x[k])
            messages[(j, i)] = messages[(i, j)]

        for i in range(num_nodes):
            x[i] = np.sum([messages[(j, i)] for j in range(num_nodes) if j != i], axis=0)
            denominator = np.sum([edge_potential(x[i], x[j]) for j in range(num_nodes) if j != i])
            if denominator != 0:
                x[i] /= denominator + 1e-8  # Add a small constant to avoid division by zero

    return x

# Example usage
original_data = np.random.randn(num_nodes)  # Generate random data
original_data = np.clip(original_data, -10, 10)  # Clip values to avoid issues

# Noise addition
noisy_data = add_noise(original_data, sigma=1.0)

# Noise removal
denoised_data = remove_noise(noisy_data, sigma=1.0)

# Visualization
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(original_data.reshape(10, 10))
plt.title("Original Data")
plt.subplot(1, 3, 2)
plt.imshow(noisy_data.reshape(10, 10))
plt.title("Noisy Data")
plt.subplot(1, 3, 3)
plt.imshow(denoised_data.reshape(10, 10))
plt.title("Denoised Data")
plt.show()