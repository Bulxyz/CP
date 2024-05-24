import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrand(theta, theta_m):
    return 1 / np.sqrt(np.sin(theta_m/2)**2 - np.sin(theta/2)**2)

def compute_ratio_integral(T0, theta_m, num_points):
    integration_points = np.linspace(0, theta_m, num_points)
    ratio = quad(integrand, 0, theta_m, args=(theta_m,), points=integration_points[:num_points-1])[0] * (T0 / np.pi)
    return ratio

def power_series_approximation(T0, theta_m):
    coeffs = [1]
    term = 1
    sum_terms = coeffs[0]

    k = 1
    while True:
        term *= (2 * k - 1) / (2 * k) * (np.sin(theta_m / 2) / 2) ** 2
        coeffs.append(term)
        sum_terms += coeffs[k]
        
        if k > 1 and np.abs(coeffs[k]) < 1e-5:
            break
        
        k += 1

    ratio = sum_terms * (T0 / np.pi)
    return ratio

# Initial values
T0 = 1.0
theta_m_values = np.linspace(0, np.pi, 100)

# Compute ratios for both solutions
ratios_integral = [compute_ratio_integral(T0, theta_m, 50) for theta_m in theta_m_values]
ratios_power_series = [power_series_approximation(T0, theta_m) for theta_m in theta_m_values]

# Plot the values
plt.plot(theta_m_values, ratios_integral, label='Integral Solution')
plt.plot(theta_m_values, ratios_power_series, label='Power Series Solution')
plt.xlabel('θm')
plt.ylabel('T/T0')
plt.title('Ratio T/T0 vs. θm')
plt.legend()
plt.show()
