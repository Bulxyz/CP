import numpy as np

# Define matrix A
A = np.array([[4, -2, 1],
              [3, 6, -4],
              [2, 1, 8]])

# Define vectors b1, b2, and b3
b1 = np.array([12, -25, 32])
b2 = np.array([4, -10, 22])
b3 = np.array([20, -30, 40])

# Solve for x1
x1 = np.linalg.solve(A, b1)

# Solve for x2
x2 = np.linalg.solve(A, b2)

# Solve for x3
x3 = np.linalg.solve(A, b3)

# Print the solutions
print("Solution for x1:", x1)
print("Solution for x2:", x2)
print("Solution for x3:", x3)
