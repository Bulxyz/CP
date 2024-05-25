import numpy as np

# Define Pauli matrices σ1, σ2, σ3
sigma_1 = np.array([[0, 1], [1, 0]])
sigma_2 = np.array([[0, -1j], [1j, 0]])
sigma_3 = np.array([[1, 0], [0, -1]])

# Define the gamma matrices γ1, γ2, γ3 based on the given expressions
gamma_1 = np.block([[np.zeros((2, 2)), sigma_1], [sigma_1, np.zeros((2, 2))]])
gamma_2 = np.block([[np.zeros((2, 2)), sigma_2], [sigma_2, np.zeros((2, 2))]])
gamma_3 = np.block([[np.eye(2), np.zeros((2, 2))], [np.zeros((2, 2)), -np.eye(2)]])

# Confirm property: γ2^dagger = -γ2
gamma_2_dagger = np.conj(gamma_2.T)
property_1 = np.allclose(gamma_2_dagger, -gamma_2)

# Confirm property: γ1 * γ2 = -i[[σ3, 0], [0, σ3]]
property_2 = np.allclose(np.dot(gamma_1, gamma_2), -1j * np.block([[sigma_3, np.zeros((2, 2))], [np.zeros((2, 2)), sigma_3]]))

# Print the results
print("Properties Verification:")
print(f"Property 1: γ2^dagger = -γ2 is {property_1}")
print(f"Property 2: γ1 * γ2 = -i[[σ3, 0], [0, σ3]] is {property_2}")
