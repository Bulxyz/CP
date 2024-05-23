import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function to fit a power-law curve
def power_law_fit(x, a, alpha):
    return a *x**alpha

# Data for trapezoid rule (N values and corresponding relative errors)
trapezoid_N_values = [2, 10, 20, 40, 80, 160, 320]
trapezoid_errors = [0.02, 0.005, 0.001, 0.0005, 0.0002, 0.0001, 0.00005]

# Data for Simpson's rule (N values and corresponding relative errors)
simpson_N_values = [2, 10, 20, 40, 80, 160, 320]
simpson_errors = [0.015, 0.003, 0.0008, 0.0003, 0.0001, 0.00005, 0.00002]

# Fit power-law curves to the data for trapezoid rule
log_trapezoid_N = np.log10(trapezoid_N_values)
log_trapezoid_errors = np.log10(trapezoid_errors)
trapezoid_popt, _ = curve_fit(power_law_fit, log_trapezoid_N, log_trapezoid_errors)

# Fit power-law curves to the data for Simpson's rule
log_simpson_N = np.log10(simpson_N_values)
log_simpson_errors = np.log10(simpson_errors)
simpson_popt, _ = curve_fit(power_law_fit, log_simpson_N, log_simpson_errors)

# Plot the log-log graphs for trapezoid and Simpson rules
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(log_trapezoid_N, log_trapezoid_errors, 'o', label='Trapezoid Rule')
plt.plot(log_trapezoid_N, power_law_fit(log_trapezoid_N, *trapezoid_popt), '--', label=f'Fit: alpha = {trapezoid_popt[1]:.2f}')
plt.xlabel('log N (Trapezoid Rule)')
plt.ylabel('log Relative Error')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(log_simpson_N, log_simpson_errors, 'o', label="Simpson's Rule")
plt.plot(log_simpson_N, power_law_fit(log_simpson_N, *simpson_popt), '--', label=f'Fit: alpha = {simpson_popt[1]:.2f}')
plt.xlabel('log N (Simpson Rule)')
plt.ylabel('log Relative Error')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
