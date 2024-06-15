import numpy as np

# Define the Breit-Wigner function
def breit_wigner(E, Er, fr, Gamma):
    return fr / ((E - Er)**2 + (Gamma/2)**2)

# Define the partial derivatives of the Breit-Wigner function
def dBW_dEr(E, Er, fr, Gamma):
    return -2 * fr * (E - Er) / ((E - Er)**2 + (Gamma/2)**2)**2

def dBW_dfr(E, Er, Gamma):
    return 1 / ((E - Er)**2 + (Gamma/2)**2)

def dBW_dGamma(E, Er, fr, Gamma):
    return -fr * Gamma / ((E - Er)**2 + (Gamma/2)**3)

# Extract data from Table 7.1
E = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200])
g = np.array([10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])
error = np.array([9.34, 17.9, 41.5, 85.5, 51.5, 21.5, 10.8, 6.29, 4.14])

# Initialize the parameters
Er_0 = 100
fr_0 = 50
Gamma_0 = 20

Er = Er_0
fr = fr_0
Gamma = Gamma_0

# Perform the Newton-Raphson algorithm
for i in range(10):
    g_fit = breit_wigner(E, Er, fr, Gamma)
    residuals = (g - g_fit) / error

    dEr = -np.sum(residuals * dBW_dEr(E, Er, fr, Gamma)) / np.sum(dBW_dEr(E, Er, fr, Gamma)**2)
    dfr = -np.sum(residuals * dBW_dfr(E, Er, Gamma)) / np.sum(dBW_dfr(E, Er, Gamma)**2)
    dGamma = -np.sum(residuals * dBW_dGamma(E, Er, fr, Gamma)) / np.sum(dBW_dGamma(E, Er, fr, Gamma)**2)

    Er = Er + dEr
    fr = fr + dfr
    Gamma = Gamma + dGamma

    print(f"Iteration {i+1}: Er = {Er:.2f}, fr = {fr:.2f}, Gamma = {Gamma:.2f}")

print(f"Final values: Er = {Er:.2f}, fr = {fr:.2f}, Gamma = {Gamma:.2f}")
