import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the second derivative using equation 5.22
def second_derivative_5_22(f, t, h):
    return (f(t + h) + f(t - h) - 2*f(t)) / (h**2)

# Function to calculate the second derivative using equation 5.23
def second_derivative_5_23(f, t, h):
    return (f(t + h) - f(t) - (f(t) - f(t - h))) / (h**2)

# Function for the cosine function
def cos_func(t):
    return np.cos(t)

# Initialize arrays to store h values and corresponding second derivatives
h_values = []
second_derivative_5_22_values = []
second_derivative_5_23_values = []

# Test the algorithms over four cycles with decreasing h values
h = np.pi / 10
machine_precision = np.finfo(float).eps
while h > machine_precision:
    h_values.append(h)
    
    # Calculate the second derivative using equation 5.22
    second_derivative_5_22_val = second_derivative_5_22(cos_func, 0, h)
    second_derivative_5_22_values.append(second_derivative_5_22_val)
    
    # Calculate the second derivative using equation 5.23
    second_derivative_5_23_val = second_derivative_5_23(cos_func, 0, h)
    second_derivative_5_23_values.append(second_derivative_5_23_val)
    
    h /= 2  # Reduce h by half for the next iteration

# Plot the results
plt.figure()
plt.plot(np.log10(h_values), np.log10(np.abs(second_derivative_5_22_values)), label='Second Derivative (Eq. 5.22)')
plt.plot(np.log10(h_values), np.log10(np.abs(second_derivative_5_23_values)), label='Second Derivative (Eq. 5.23)')
plt.xlabel('log10 h')
plt.ylabel('log10 |Second Derivative|')
plt.legend()
plt.grid(True)
plt.show()
