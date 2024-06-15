import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Extract data from Table 7.1
E = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200])
g = np.array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])
error = np.array([9.34, 17.9, 41.5, 85.5, 51.5, 21.5, 10.8, 6.29, 4.14])

# Define the Breit-Wigner function
def breit_wigner(E, Er, fr, Gamma):
    return fr / ((E - Er)**2 + (Gamma/2)**2)

# Use curve_fit to find the best-fit parameters
popt, pcov = curve_fit(breit_wigner, E, g, sigma=error, p0=[100, 50, 20])
Er, fr, Gamma = popt

# Evaluate the quality of the fit
g_fit = breit_wigner(E, Er, fr, Gamma)
residuals = (g - g_fit) / error
chi_square = np.sum(residuals**2)
dof = len(E) - 3  # Degrees of freedom

print(f"Er = {Er:.2f}")
print(f"fr = {fr:.2f}")
print(f"Gamma = {Gamma:.2f}")
print(f"Chi-square: {chi_square:.2f} (dof = {dof})")

# Plot the experimental data and the fitted Breit-Wigner curve
plt.figure(figsize=(8, 6))
plt.errorbar(E, g, yerr=error, fmt='o', label='Experimental data')
plt.plot(E, breit_wigner(E, Er, fr, Gamma), label='Breit-Wigner fit')
plt.xlabel('Energy (MeV)')
plt.ylabel('Scattering cross section (mb)')
plt.title('Breit-Wigner Fit to Experimental Data')
plt.legend()
plt.show()
