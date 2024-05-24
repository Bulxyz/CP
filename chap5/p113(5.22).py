import numpy as np
import matplotlib.pyplot as plt

def von_neumann_rejection():
    while True:
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        v1 = 2 * u1 - 1
        v2 = 2 * u2 - 1
        squared_sum = v1**2 + v2**2

        if squared_sum <= 1 and squared_sum > 0:
            x = v1 * np.sqrt(-2 * np.log(squared_sum) / squared_sum)
            return x

# Generate samples using both methods
sample_size = 100000
von_neumann_samples = [von_neumann_rejection() for _ in range(sample_size)]
gaussian_samples = np.random.normal(0, 1, sample_size)

# Plot histograms
plt.hist(von_neumann_samples, bins=100, alpha=0.5, label='von Neumann Rejection')
plt.hist(gaussian_samples, bins=100, alpha=0.5, label='Gaussian Method')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Comparison of von Neumann Rejection and Gaussian Method')
plt.legend()
plt.show()

# Calculate mean and standard deviation
von_neumann_mean = np.mean(von_neumann_samples)
von_neumann_std = np.std(von_neumann_samples)
gaussian_mean = np.mean(gaussian_samples)
gaussian_std = np.std(gaussian_samples)

# Print results
print('von Neumann Rejection - Mean:', von_neumann_mean, 'Standard Deviation:', von_neumann_std)
print('Gaussian Method - Mean:', gaussian_mean, 'Standard Deviation:', gaussian_std)
