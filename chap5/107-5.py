import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrand(phi, k):
    return 1 / np.sqrt(1 - k**2 * np.sin(phi)**2)

def potential(z, V, a):
    k = 2 * a / np.sqrt(z**2 + 4 * a**2)
    integral, _ = quad(integrand, 0, np.pi/2, args=(k,))
    return V/2 * (1 - k * z / (np.pi * a) * integral)

# Parameters
V = 1
a = 1
z_values = np.linspace(0.05, 10, 100)

# Calculate potential for each z value
potential_values = [potential(z, V, a) for z in z_values]

# Calculate 1/r potential for comparison
r_values = np.sqrt(z_values**2 + 4 * a**2)
potential_1_over_r = V / r_values

# Plot the potential
plt.plot(z_values, potential_values, label='Potential')
plt.plot(z_values, potential_1_over_r, label='1/r Fall-off')
plt.xlabel('z')
plt.ylabel('Potential')
plt.title('Potential vs. z')
plt.legend()
plt.show()
