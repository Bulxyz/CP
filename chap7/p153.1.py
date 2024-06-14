import numpy as np

def lagrange_interpolation(x_data, y_data, x_interp):
    """
    Performs n-point Lagrange interpolation.

    Parameters:
    x_data (numpy.ndarray): Array of independent variable data points.
    y_data (numpy.ndarray): Array of dependent variable data points.
    x_interp (numpy.ndarray): Array of independent variable points to interpolate.

    Returns:
    numpy.ndarray: Array of interpolated dependent variable values.
    """
    n = len(x_data)
    y_interp = []

    for x in x_interp:
        lagrange_sum = 0
        for i in range(n):
            numerator = 1
            denominator = 1
            for j in range(n):
                if j != i:
                    numerator *= (x - x_data[j])
                    denominator *= (x_data[i] - x_data[j])
            lagrange_sum += y_data[i] * (numerator / denominator)
        y_interp.append(lagrange_sum)

    return np.array(y_interp)



# Data from the table
x_data = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200])
y_data = np.array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])

# Interpolate at new points
x_interp = np.linspace(0, 200, 50)
y_interp = lagrange_interpolation(x_data, y_data, x_interp)

# Plot the results
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.plot(x_data, y_data, 'ro', label='Data Points')
plt.plot(x_interp, y_interp, 'b-', label='Interpolated')
plt.xlabel('E_i (MeV)')
plt.ylabel('g(E_i) (mb)')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid()
plt.show()
