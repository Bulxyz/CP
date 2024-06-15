import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the exponential decay function
def exponential_decay(t, N0, tau):
    return N0 * np.exp(-t / tau)

# Sample data points derived from the graph (manually read from Figure 7.6)
time_bins = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
number_of_events = np.array([35, 28, 22, 16, 12, 9, 6, 4, 3, 2, 1])

# Initial guess parameters
initial_guess = [number_of_events[0], 20]

# Perform the curve fit
params, covariance = curve_fit(exponential_decay, time_bins, number_of_events, p0=initial_guess)
N0_fit, tau_fit = params
print(f"Fitted parameter N0: {N0_fit}")
print(f"Fitted parameter tau: {tau_fit}")

# Calculated fitted values
fitted_values = exponential_decay(time_bins, N0_fit, tau_fit)

# Derivative at t = 0
dN0_dt = -N0_fit / tau_fit
print(f"Derivative at t=0: {dN0_dt}")

# Plot the data and the fit
plt.figure()
plt.plot(time_bins, number_of_events, 'bs-', label='data')
plt.plot(time_bins, fitted_values, 'r--', label='fit')
plt.xlabel('Time [ns]')
plt.ylabel('Number')
plt.legend()
plt.title('Exponential Decay Fit')
plt.show()

# Construct the table of values (ΔN/Δt, t, σ)
time_mid_bins = time_bins - 5  # Assuming the middle of each 10ns bin
delta_N = -np.diff(number_of_events)  # ΔN (difference between consecutive bins)
delta_t = 10  # Δt (time interval between bins)
delta_N_delta_t = delta_N / delta_t
sigma = np.sqrt(number_of_events[:-1])  # Error estimate using square root of number of events

# Construct the table
table = np.stack((delta_N_delta_t, time_mid_bins[:-1], sigma), axis=-1)
print("Table of (ΔN/Δt ± σ, t) values:")
print(table)
