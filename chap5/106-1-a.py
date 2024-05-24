import numpy as np
from scipy.integrate import simps, quad

# Define the functions to be integrated
def f1(x):
    return np.sin(100*x)

def f2(x):
    return np.sin(100*x)**x

# Integration limits
a = 0
b = 2*np.pi

# Number of points for integration
N = 1000

# Generate evenly spaced x values for the non-problematic region
x_non_problematic = np.linspace(1e-8, b, N+1)

# Generate x values specifically for the problematic region near zero
x_problematic = np.linspace(a, 1e-8, N//10+1)

# Custom piecewise integration for F2
integral_F2_non_problematic = simps(f2(x_non_problematic), x_non_problematic)

# Define the custom integration method for the problematic region
def custom_integration_method_for_problematic_region(f, x):
    return quad(f, a, b)[0]

# Apply the custom integration method for the problematic region
integral_F2_problematic = custom_integration_method_for_problematic_region(f2, x_problematic)

# Combine the results from both parts
integral_F2 = integral_F2_non_problematic + integral_F2_problematic

# Print the results
print("Results:")
print(f"Integral F1 using Simpson's Rule: {simps(f1(x_non_problematic), x_non_problematic)}")
print(f"Integral F2 using Custom Piecewise Integration: {integral_F2}")
