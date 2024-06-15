import numpy as np

# Data points
x = np.array([0, 1, 2, 3])
y = np.array([1, 3, 7, 15])

# Number of data points and parameters
n = len(x)
p = 3  # Number of parameters (a1, a2, a3)

# Design matrix
X = np.column_stack((np.ones_like(x), x, x**2))

# Least-squares solution
a = np.linalg.lstsq(X, y, rcond=None)[0]

print(f"a1 = {a[0]:.2f}")
print(f"a2 = {a[1]:.2f}")
print(f"a3 = {a[2]:.2f}")

# Calculate chi-square
y_pred = a[0] + a[1]*x + a[2]*x**2
residuals = y - y_pred
chi_square = np 
