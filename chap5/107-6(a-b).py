import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrand(phi, k):
    return np.sqrt(1 - k**2 * np.sin(phi)**2)

def elliptic_integral_K(k):
    integral, _ = quad(integrand, 0, np.pi/2, args=(k,))
    return integral

def elliptic_integral_E(k):
    integrand_func = lambda phi: np.sqrt(1 - k**2 * np.sin(phi)**2)
    integral, _ = quad(integrand_func, 0, np.pi/2)
    return integral

def vector_potential(r, theta, a, I):
    mu_0_over_4pi = 1
    k_squared = (4 * a * r * np.sin(theta)) / (a**2 + r**2 + 2 * a * r * np.sin(theta))
    k = np.sqrt(k_squared)
    K = elliptic_integral_K(k)
    E = elliptic_integral_E(k)
    A_phi = (mu_0_over_4pi * 4 * I * a / np.sqrt(a**2 + r**2 + 2 * a * r * np.sin(theta))) * ((2 - k_squared) * K - 2 * E) / k_squared
    return A_phi

# Parameters
a = 1
I = 3
mu_0_over_4pi = 1
r = 1.1
theta_values = np.linspace(0, np.pi, 100)

# Compute A_phi for each theta value
A_phi_values = [vector_potential(r, theta, a, I) for theta in theta_values]

# Plot A_phi vs. theta
plt.plot(theta_values, A_phi_values)
plt.xlabel('θ')
plt.ylabel('A_φ')
plt.title('A_φ vs. θ')
plt.show()
#####################################################################################
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def integrand(phi, k):
    return np.sqrt(1 - k**2 * np.sin(phi)**2)

def elliptic_integral_K(k):
    integral, _ = quad(integrand, 0, np.pi/2, args=(k,))
    return integral

def elliptic_integral_E(k):
    integrand_func = lambda phi: np.sqrt(1 - k**2 * np.sin(phi)**2)
    integral, _ = quad(integrand_func, 0, np.pi/2)
    return integral

def vector_potential(r, theta, a, I):
    mu_0_over_4pi = 1
    k_squared = (4 * a * r * np.sin(theta)) / (a**2 + r**2 + 2 * a * r * np.sin(theta))
    k = np.sqrt(k_squared)
    K = elliptic_integral_K(k)
    E = elliptic_integral_E(k)
    A_phi = (mu_0_over_4pi * 4 * I * a / np.sqrt(a**2 + r**2 + 2 * a * r * np.sin(theta))) * ((2 - k_squared) * K - 2 * E) / k_squared
    return A_phi

# Parameters
a = 1
I = 3
mu_0_over_4pi = 1
theta = np.pi / 3
r_values = np.linspace(0.1, 10, 100)

# Compute A_phi for each r value
A_phi_values = [vector_potential(r, theta, a, I) for r in r_values]

# Plot A_phi vs. r
plt.plot(r_values, A_phi_values)
plt.xlabel('r')
plt.ylabel('A_φ')
plt.title('A_φ vs. r at θ=π/3')
plt.show()
