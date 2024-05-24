import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integration(dimensions, sample_size):
    integral_sum = 0

    for _ in range(sample_size):
        x = np.random.random(dimensions)
        integral_sum += np.sum(x) ** 2

    integral_average = integral_sum / sample_size
    return integral_average

def calculate_relative_error(true_value, estimated_value):
    return np.abs(estimated_value - true_value) / true_value

# True value of the integral
true_value = 385 / 6

# Parameters
trials = 16
sample_sizes = 2 ** np.arange(1, 14)  # N = 2, 4, 8, ..., 8192

# Perform Monte Carlo integration and calculate relative errors
relative_errors = []

for sample_size in sample_sizes:
    trial_results = []

    for _ in range(trials):
        estimated_value = monte_carlo_integration(10, sample_size)
        relative_error = calculate_relative_error(true_value, estimated_value)
        trial_results.append(relative_error)

    average_relative_error = np.mean(trial_results)
    relative_errors.append(average_relative_error)

# Plot the relative errors
plt.plot(1 / np.sqrt(sample_sizes), relative_errors)
plt.xlabel('1 / √N')
plt.ylabel('Relative Error')
plt.title('Relative Error vs. 1 / √N')
plt.show()
