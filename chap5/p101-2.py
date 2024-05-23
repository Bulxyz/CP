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

# Function to calculate relative error
def relative_error(numerical, exact):
    return np.abs((numerical - exact) / exact)

# Compute relative error for different N values
N_values = [2**i for i in range(1, 11)]
results = []
for N in N_values:
    trapezoid_result = trapezoid_rule_integration(f, 0, 1, N)
    simpson_result = simpson_integration(f, 0, 1, N)
    gaussian_result = gaussian_quadrature_integration(f, 0, 1, N)
    
    trapezoid_error = relative_error(trapezoid_result, analytical_solution)
    simpson_error = relative_error(simpson_result, analytical_solution)
    gaussian_error = relative_error(gaussian_result, analytical_solution)
    
    results.append((N, trapezoid_error, simpson_error, gaussian_error))

# Print the results in tabular form
print("N\tTrapezoid Error\tSimpson Error\tGaussian Error")
for result in results:
    print(f"{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}")
