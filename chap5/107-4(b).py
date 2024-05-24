import numpy as np

def power_series_approximation(T0, theta_m):
    # Coefficients of the power series expansion
    coeffs = [1]
    term = 1
    sum_terms = coeffs[0]

    # Compute the power series approximation
    k = 1
    while True:
        term *= (2 * k - 1) / (2 * k) * (np.sin(theta_m / 2) / 2) ** 2
        coeffs.append(term)
        sum_terms += coeffs[k]
        
        # Check if changes occur only in the fifth decimal place or beyond
        if k > 1 and np.abs(coeffs[k]) < 1e-5:
            break
        
        k += 1

    ratio = sum_terms * (T0 / np.pi)
    return ratio

# Initial values
T0 = 1.0
theta_m_values = np.linspace(0, np.pi, 5)

# Loop through different values of theta_m
for theta_m in theta_m_values:
    ratio = power_series_approximation(T0, theta_m)
    print(f"theta_m = {theta_m:.4f}, ratio = {ratio:.4f}")
