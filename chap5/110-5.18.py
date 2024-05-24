import numpy as np
import matplotlib.pyplot as plt

def gaussian_integrand(x):
    return np.exp(-x**2)  # Example of a Gaussian integrand

def proposal_distribution(x):
    return np.exp(-x**2)  # Using a Gaussian proposal distribution

def monte_carlo_integration_importance_sampling(sample_size):
    integral_sum = 0

    for _ in range(sample_size):
        x = np.random.normal(0, 1)  # Sample from the Gaussian proposal distribution
        weight = gaussian_integrand(x) / proposal_distribution(x)
        integral_sum += weight

    integral_average = integral_sum / sample_size
    return integral_average

# True value of the integral (in this case, it's the known value of the Gaussian integral)
true_value = np.sqrt(np.pi)

# Parameters
trials = 16
sample_sizes = 2 ** np.arange(1, 14)  # N = 2, 4, 8, ..., 8192

# Perform Monte Carlo integration with importance sampling and calculate relative errors
relative_errors = []

for sample_size in sample_sizes:
    trial_results = []

    for _ in range(trials):
        estimated_value = monte_carlo_integration_importance_sampling(sample_size)
        relative_error = np.abs(estimated_value - true_value) / true_value
        trial_results.append(relative_error)

    average_relative_error = np.mean(trial_results)
    relative_errors.append(average_relative_error)

# Plot the relative errors
plt.plot(1 / np.sqrt(sample_sizes), relative_errors)
plt.xlabel('1 / √N')
plt.ylabel('Relative Error')
plt.title('Relative Error vs. 1 / √N (Importance Sampling)')
plt.show()
