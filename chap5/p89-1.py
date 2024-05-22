import numpy as np
def forward_diff(f, t, h):
    return (f(t + h) - f(t)) / h

def central_diff(f, t, h):
    return (f(t + h/2) - f(t - h/2)) / h

def extrapolated_diff(f, t, h):
    return (8*(f(t + h/4) - f(t - h/4)) - (f(t + h/2) - f(t - h/2))) / (3*h)

def f(x):
    # Define your function here
    return x**2

def df(x):
    # Define the derivative of your function here
    return 2*x

x = 1.0  # Point at which to differentiate
h = 1.0  # Initial step size
eps = np.finfo(float).eps  # Machine precision

while h > eps:
    fd = forward_diff(f, x, h)
    cd = central_diff(f, x, h)
    ed = extrapolated_diff(f, x, h)
    
    exact = df(x)
    
    fd_error = abs((fd - exact) / exact)
    cd_error = abs((cd - exact) / exact)
    ed_error = abs((ed - exact) / exact)
    
    print(f"h: {h}, Forward Diff: {fd}, Error: {fd_error}")
    print(f"h: {h}, Central Diff: {cd}, Error: {cd_error}")
    print(f"h: {h}, Extrapolated Diff: {ed}, Error: {ed_error}")
    print()
    
    h /= 2  # Reduce the step size
######################################################################################
import numpy as np
import matplotlib.pyplot as plt

# Define the functions for forward, central, and extrapolated differentiation
def forward_diff(f, t, h):
    return (f(t + h) - f(t)) / h

def central_diff(f, t, h):
    return (f(t + h/2) - f(t - h/2)) / h

def extrapolated_diff(f, t, h):
    return (8

*(f(t + h/4) - f(t - h/4)) - (f(t + h/2) - f(t - h/2))) / (3*

h)

# Define the function f(x) for differentiation
def f(x):
    return np.sin(x)  # Example function, you can replace with any function

# Define the true derivative of f(x) for error calculation
def true_derivative(x):
    return np.cos(x)  # True derivative of the example function

# Define the range of h values for calculation
h_values = np.logspace(-10, 0, 100)

# Calculate the errors for each differentiation method at different h values
errors_forward = np.abs(forward_diff(f, 1, h_values) - true_derivative(1))
errors_central = np.abs(central_diff(f, 1, h_values) - true_derivative(1))
errors_extrapolated = np.abs(extrapolated_diff(f, 1, h_values) - true_derivative(1))

# Plot log10 |𝜖| vs. log10 h
plt.figure()
plt.loglog(h_values, errors_forward, label='Forward Difference')
plt.loglog(h_values, errors_central, label='Central Difference')
plt.loglog(h_values, errors_extrapolated, label='Extrapolated Difference')
plt.xlabel('log10 h')
plt.ylabel('log10 |𝜖|')
plt.legend()
plt.grid(True)
plt.show()
########################################################################################



