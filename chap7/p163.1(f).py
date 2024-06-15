import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the linear function
def linear_function(x, m, b):
    return m * x + b

# Sample data points derived from the graph (manually read from Figure 7.6)
time_bins = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
number_of_events = np.array([35, 28, 22, 16, 12, 9, 6, 4, 3, 2, 1])

# Construct the table of values (ΔN/Δt, t, σ)
time_mid_bins = time_bins[:-1] - 5  # Assuming the middle of each 10ns bin
delta_N = -np.diff(number_of_events)  # ΔN (difference between consecutive bins)
delta_t = 10  # Δt (time interval between bins)
delta_N_delta_t = delta_N / delta_t
sigma = np.sqrt(number_of_events[:-1])  # Error estimate using square root of number of events

# Perform the linear fit
params, covariance = curve_fit(linear_function, time_mid_bins, np.log(np.abs(delta_N_delta_t)))
m, b = params
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Calculate the lifetime τ
tau = -1 / m
print(f"Lifetime τ: {tau:.2e} s")

# Compare to the tabulated lifetime
tabulated_lifetime = 2.6e-8
print(f"Tabulated lifetime: {tabulated_lifetime:.2e} s")
print(f"Difference: {(tau - tabulated_lifetime) / tabulated_lifetime * 100:.2f}%")

# Plot the data and the fit
plt.figure()
plt.plot(time_mid_bins, np.log(np.abs(delta_N_delta_t)), 'bs-', label='data')
plt.plot(time_mid_bins, linear_function(time_mid_bins, m, b), 'r--', label='fit')
plt.xlabel('Time [ns]')
plt.ylabel('ln|ΔN/Δt|')
plt.legend()
plt.title('ln|ΔN/Δt| vs. Time with Linear Fit')
plt.show()
