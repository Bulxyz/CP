import numpy as np

# Function to calculate the second derivative using equation 5.22
def second_derivative_5_22(f, t, h):
    return (f(t + h) + f(t - h) - 2*f(t)) / (h**2)

# Function to calculate the second derivative using equation 5.23
def second_derivative_5_23(f, t, h):
    return (f(t + h) - f(t) - (f(t) - f(t - h))) / (h**2)

# Function for the cosine function
def cos_func(t):
    return np.cos(t)

# Test the algorithms over four cycles with decreasing h values
h = np.pi / 10
machine_precision = np.finfo(float).eps
while h > machine_precision:
    print(f"h = {h}")
    
    # Calculate the second derivative using equation 5.22
    second_derivative_5_22_val = second_derivative_5_22(cos_func, 0, h)
    print(f"Second Derivative (Eq. 5.22): {second_derivative_5_22_val}")
    
    # Calculate the second derivative using equation 5.23
    second_derivative_5_23_val = second_derivative_5_23(cos_func, 0, h)
    print(f"Second Derivative (Eq. 5.23): {second_derivative_5_23_val}")
    
    h /= 2  # Reduce h by half for the next iteration
