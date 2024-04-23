def calculate_S1(N):
    result = 0.0
    for n in range(1, 2*N+1):
        result += ((-1)**n) * n / (n + 1)
    return result

# Define the value of N
N = 100

# Calculate S(1) for the given N
S1 = calculate_S1(N)

print(f"The value of S(1) for N = {N} is: {S1}")



################################################

