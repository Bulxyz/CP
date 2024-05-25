"""copy-paste each part separately"""

#part(a)
import numpy as np

# Define the matrix A
A = np.array([[-2, 2, -3],
              [2, 1, -6],
              [-1, -2, 0]])

# Find the eigenvalues
eigenvalues = np.linalg.eig(A)[0]

# Print the eigenvalues
print("Eigenvalues of A:", eigenvalues)
#######################################################
#part(b)
import numpy as np
# Define the eigenvalue and eigenvector
eigenvalue = 5
eigenvector = np.array([-1, -2, 1]) / np.sqrt(6)

# Calculate the product of eigenvector and eigenvalue
product = eigenvalue * eigenvector

# Verify if the product is equal to the eigenvalue
is_equal = np.allclose(product, eigenvalue * eigenvector)

# Print the result
print("Is the product equal to the eigenvalue?", is_equal)
########################################################
#part(c)
import numpy as np
# Define the matrix A
A = np.array([[-2, 2, -3],
              [2, 1, -6],
              [-1, -2, 0]])

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the indices of eigenvalues equal to -3
indices = np.where(np.isclose(eigenvalues, -3))[0]

# Extract the corresponding eigenvectors
computed_eigenvectors = eigenvectors[:, indices]

# Calculate the linear combination of the two given eigenvectors
linear_combination = np.sqrt(5) * computed_eigenvectors[:, 0] - np.sqrt(10) * computed_eigenvectors[:, 1]

# Verify if the linear combination matches the given eigenvectors
is_match = np.allclose(linear_combination, np.zeros_like(linear_combination))

# Print the result
print("Is the linear combination equal to zero?", is_match)
