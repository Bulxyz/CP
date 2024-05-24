import numpy as np
from scipy.integrate import quad

def integrand(theta, theta_m):
    return 1 / np.sqrt(np.sin(theta_m/2)**2 - np.sin(theta/2)**2)

def compute_ratio(T0, theta_m, num_points):
    integration_points = np.linspace(0, theta_m, num_points)
    ratio = quad(integrand, 0, theta_m, args=(theta_m,), points=integration_points)[0] * (T0 / np.pi)
    return ratio

# Initial values
T0 = 1.0
theta_m_values = np.linspace(0, np.pi, 5)

# Loop through different values of theta_m
for theta_m in theta_m_values:
    num_points = 10  # Start with 10 integration points
    ratio_prev = compute_ratio(T0, theta_m, num_points)
    num_points *= 2  # Double the number of integration points
    ratio_curr = compute_ratio(T0, theta_m, num_points)

    # Increasing the number of integration points until changes occur only in the fifth decimal place or beyond
    while np.abs(ratio_curr - ratio_prev) >= 1e-5:
        ratio_prev = ratio_curr
        num_points *= 2
        ratio_curr = compute_ratio(T0, theta_m, num_points)

    print(f"theta_m = {theta_m:.4f}, ratio = {ratio_curr:.4f}")
