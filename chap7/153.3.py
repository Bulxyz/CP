import numpy as np
import matplotlib.pyplot as plt

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

# Fit the entire spectrum with an eight-degree polynomial
x_interp = np.linspace(0, 200, 41)  # Interpolate in steps of 5 MeV
y_interp = lagrange_interpolation(x_data, y_data, x_interp)

# Locate the peak position
peak_idx = np.argmax(y_interp)
peak_energy = x_interp[peak_idx]
print(f"Resonance energy (Er) from interpolation: {peak_energy:.2f} MeV")

# Determine the full-width at half-maximum (FWHM)
half_max = np.max(y_interp) / 2
left_idx = np.searchsorted(y_interp, half_max, side='left')
right_idx = np.searchsorted(y_interp, half_max, side='right')
fwhm = x_interp[right_idx] - x_interp[left_idx]
print(f"Full-width at half-maximum (Γ) from interpolation: {fwhm:.2f} MeV")

# Compare with the theorist's prediction
theorist_Er = 78
theorist_Gamma = 55
print(f"Theorist's prediction: (Er, Γ) = ({theorist_Er}, {theorist_Gamma}) MeV")
