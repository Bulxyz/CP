import numpy as np

# Define the matrix A
alpha = 2
beta = 3
A = np.array([[alpha, beta],
              [-beta, alpha]])

# Find the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the eigenvalues and eigenvectors
for i in range(len(eigenvalues)):
    print("Eigenvalue", i+1, ":", eigenvalues[i])
    print("Eigenvector", i+1, ":", eigenvectors[:, i])
    print()
