import numpy as np
import matplotlib.pyplot as plt

# Data from Table 7.2
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
T = np.array([14.6, 18.5, 36.6, 30.8, 59.2, 60.1, 62.2, 79.4, 99.9])

# Fit a linear function T(x) = a + bx
coefficients = np.polyfit(x, T, 1)
a, b = coefficients
print(f"Linear fit: T(x) = {a:.2f} + {b:.2f}x")

# Plot the data and the linear fit
plt.figure(figsize=(8, 6))
plt.plot(x, T, 'bo-', label='Data')
plt.plot(x, a + b*x, 'r--', label='Linear fit')
plt.xlabel('Distance, x (cm)')
plt.ylabel('Temperature, T (°C)')
plt.title('Temperature vs. Distance along a Metal Rod')
plt.legend()
plt.grid()
plt.show()
