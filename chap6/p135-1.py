import numpy as np

# Define matrix A
A = np.array([[4, -2, 1],
              [3, 6, -4],
              [2, 1, 8]])

# Find the numerical inverse of A
A_inv = np.linalg.inv(A)

# Print the result
print(A_inv)
error = np.dot(A, A_inv) - np.eye(3)
print(error)
