import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Function to be integrated
def f(t):
    return np.exp(-t)

# Analytical solution
analytical_solution = 1 - np.exp(-1)

# Trapezoid rule integration
def trapezoid_rule_integration(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h *(0.5*f(a) + 0.5*f(b) + np.sum(f(x[1:-1])))

# Function to calculate relative error
def relative_error(numerical, exact):
    return np.abs((numerical - exact) / exact)

# Compute relative error for different N values
N_values = [2**i for i in range(1, 11)]
results = []
for N in N_values:
    trapezoid_result = trapezoid_rule_integration(f, 0, 1, N)
    trapezoid_error = relative_error(trapezoid_result, analytical_solution)
    results.append((N, trapezoid_error))

# Extract N values and relative errors for plotting
N_values = [result[0] for result in results]
errors = [result[1] for result in results]

# Fit a power-law curve to the data in log-log space
log_N = np.log10(N_values)
log_errors = np.log10(errors)

def power_law_fit(x, a, alpha):
    return a *x**alpha

popt, pcov = curve_fit(power_law_fit, log_N, log_errors)

# Plot the log-log graph
plt.figure()
plt.plot(log_N, log_errors, 'o', label='Relative Error vs. N')
plt.plot(log_N, power_law_fit(log_N, *popt), '--', label=f'Fit: alpha = {popt[1]:.2f}')
plt.xlabel('log N')
plt.ylabel('log Relative Error')
plt.legend()
plt.grid(True)
plt.show()
