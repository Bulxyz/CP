import numpy as np
from scipy.integrate import quad

def elliptic_integral_first_kind(theta, m):
    """Integrand for the elliptic integral of the first kind."""
    return 1 / np.sqrt(1 - m * np.sin(theta)**2)

def compute_K(m):
    """Compute the elliptic integral of the first kind for a given m."""
    # Integration limits
    a = 0
    b = np.pi / 2

    # Numerical integration
    result, error = quad(elliptic_integral_first_kind, a, b, args=(m,))
    return result

def polynomial_approximation(m):
    """Compute the polynomial approximation for the elliptic integral of the first kind."""
    # Coefficients of the Taylor series expansion
    coeffs = [1, 1/4, 9/64, 25/256, 1225/16384]

    # Compute the polynomial approximation
    poly_K = np.pi / 2 * sum(coeffs[i] * m**i for i in range(len(coeffs)))
    return poly_K

# Example value of m
m = 0.5

# Compute K(m) using numerical integration
K_m = compute_K(m)

# Compute the polynomial approximation for K(m)
poly_K_m = polynomial_approximation(m)

# Compute the difference between the numerical and polynomial results
difference = abs(K_m - poly_K_m)

# Define the tolerance
tolerance = 3e-2

# Output the results and comparison
print(f"Computed K({m}) = {K_m}")
print(f"Polynomial approximation = {poly_K_m}")
print(f"Difference = {difference}")

if difference <= tolerance:
    print("The numerical result is within the desired tolerance of the polynomial approximation.")
else:
    print("The numerical result is not within the desired tolerance. Consider adjusting the polynomial or integration parameters.")
