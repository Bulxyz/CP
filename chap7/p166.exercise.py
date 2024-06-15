import numpy as np

# Sample data from Figure 7.6
t = np.array([5.0, 15.0, 25.0, 35.0, 45.0, 55.0, 65.0, 75.0, 85.0, 95.0, 105.0])
dN_dt = np.array([7.0, 6.0, 6.0, 4.0, 3.0, 3.0, 2.0, 1.0, 1.0, 1.0, 1.0])
sigma = np.sqrt(dN_dt)

# Define the functions
def g(x, N0, tau):
    return N0 * np.exp(-x / tau)

def dg_da1(x, N0, tau):
    return np.exp(-x / tau)

def dg_da2(x, N0, tau):
    return -N0 / tau * np.exp(-x / tau)

def dg_da3(x, N0, tau):
    return N0 / tau**2 * np.exp(-x / tau)

# Compute the sums
S = np.sum(1 / sigma**2)
Sx = np.sum(t / sigma**2)
Sxx = np.sum(t**2 / sigma**2)
Sxxx = np.sum(t**3 / sigma**2)
Sxxxx = np.sum(t**4 / sigma**2)
Sy = np.sum(dN_dt / sigma**2)
Sxy = np.sum(t * dN_dt / sigma**2)
Sxxy = np.sum(t**2 * dN_dt / sigma**2)

# Solve the system of equations
A = np.array([[S, Sx, Sxx], [Sx, Sxx, Sxxx], [Sxx, Sxxx, Sxxxx]])
b = np.array([Sy, Sxy, Sxxy])
x = np.linalg.solve(A, b)

N0 = x[0]
tau = -1 / x[1]

print(f"N0 = {N0:.2f}")
print(f"tau = {tau:.2f}")
