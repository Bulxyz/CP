import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 1.38e-23  # Boltzmann constant in J/K
mu = 9.27e-24  # Magnetic moment in J/T (approximately for an electron)
N = 1e23  # Number of particles (example value)
lambda_ = 1e-3  # Molecular field constant (example value)

# Self-consistent equation for magnetization M(T)
def magnetization(T, initial_guess=1e-20, tol=1e-6, max_iter=100, backtrack_factor=0.5, max_backtracks=10):
    def f(M):
        return M - N * mu * np.tanh(lambda_ * mu * M / (k_B * T))
    
    def df(M):
        return 1 - N * mu * lambda_ * mu / (k_B * T) * (1 - np.tanh(lambda_ * mu * M / (k_B * T))**2)
    
    # Newton-Raphson with backtracking
    M = initial_guess
    for _ in range(max_iter):
        f_M = f(M)
        df_M = df(M)
        if np.isnan(f_M) or np.isnan(df_M):
            raise ValueError(f"Newton-Raphson failed due to invalid function or derivative value at M = {M}")

        M_new = M - f_M / df_M

        # Backtracking
        backtracks = 0
        while np.isnan(f(M_new)) or np.abs(f(M_new)) > np.abs(f_M):
            M_new = M - backtrack_factor * (f_M / df_M)
            backtrack_factor *= 0.5
            backtracks += 1
            if backtracks > max_backtracks:
                raise ValueError("Newton-Raphson with backtracking did not converge")

        if abs(M_new - M) < tol:
            return M_new
        M = M_new
    raise ValueError("Newton-Raphson with backtracking did not converge")

# Range of temperatures
temperatures = np.linspace(1, 300, 100)  # Temperature range from 1 K to 300 K

# Calculate magnetization for each temperature
magnetizations = []
for T in temperatures:
    try:
        M = magnetization(T)
        magnetizations.append(M)
    except ValueError as e:
        magnetizations.append(np.nan)
        print(f"Failed to find solution at T = {T}: {e}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(temperatures, magnetizations, label='Magnetization M(T)')
plt.xlabel('Temperature (K)')
plt.ylabel('Magnetization (A/m)')
plt.title('Magnetization as a Function of Temperature')
plt.legend()
plt.grid(True)
plt.show()
