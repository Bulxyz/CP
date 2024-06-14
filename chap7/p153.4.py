import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_data, y_data, x_interp):
    """
    Performs three-point Lagrange interpolation.

    Parameters:
    x_data (numpy.ndarray): Array of independent variable data points (3 points).
    y_data (numpy.ndarray): Array of dependent variable data points (3 points).
    x_interp (float): Independent variable point to interpolate.

    Returns:
    float: Interpolated dependent variable value.
    """
    n = len(x_data)
    if n != 3:
        raise ValueError("Lagrange interpolation requires 3 data points.")

    x1, x2, x3 = x_data
    y1, y2, y3 = y_data

    numerator = y1 * (x_interp - x2) * (x_interp - x3)
    denominator = (x1 - x2) * (x1 - x3)
    term1 = numerator / denominator

    numerator = y2 * (x_interp - x1) * (x_interp - x3)
    denominator = (x2 - x1) * (x2 - x3)
    term2 = numerator / denominator

    numerator = y3 * (x_interp - x1) * (x_interp - x2)
    denominator = (x3 - x1) * (x3 - x2)
    term3 = numerator / denominator

    return term1 + term2 + term3

# Generate 3 random data points
x_data = np.random.uniform(0, 100, 3)
y_data = np.random.uniform(0, 100, 3)

# Interpolate a new point
x_interp = np.random.uniform(0, 100)
y_interp = lagrange_interpolation(x_data, y_data, x_interp)

print("Data points:")
for i in range(3):
    print(f"x{i+1} = {x_data[i]:.2f}, y{i+1} = {y_data[i]:.2f}")

print(f"\nInterpolated value at x = {x_interp:.2f} is {y_interp:.2f}")

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.plot([x_interp], [y_interp], 'bx', label='Interpolated')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Three-Point Lagrange Interpolation')
plt.legend()
plt.grid()
plt.show()
