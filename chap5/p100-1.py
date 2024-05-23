import numpy as np
from scipy.integrate import quad
from scipy.integrate import simps
from numpy.polynomial.legendre import leggauss

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
    return h * (0.5*f(a) + 0.5*f(b) + np.sum(f(x[1:-1])))

# Simpson's rule integration
def simpson_integration(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return simps(y, x)

# Gaussian quadrature integration
def gaussian_quadrature_integration(f, a, b, n):
    x, w = leggauss(n)
    res = 0
    for i in range(n):
        res += w[i] * f(0.5 * (b - a) * x[i] + 0.5 * (b + a))
    return 0.5 * (b - a) * res

# Numerical integration using different methods
trapezoid_result = trapezoid_rule_integration(f, 0, 1, 1000)
simpson_result = simpson_integration(f, 0, 1, 1000)
gaussian_result = gaussian_quadrature_integration(f, 0, 1, 5)

# Compare with analytical solution
print(f"Analytical Solution: {analytical_solution}")
print(f"Trapezoid Rule Result: {trapezoid_result}")
print(f"Simpson's Rule Result: {simpson_result}")
print(f"Gaussian Quadrature Result: {gaussian_result}")
