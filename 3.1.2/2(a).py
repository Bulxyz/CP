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
def calculate_S2(N):
    sum1 = 0.0
    sum2 = 0.0
    
    # Calculate the first sum: - sum over n=1 to N of (2n-1 / n)
    for n in range(1, N+1):
        sum1 -= (2*n - 1) / n
    
    # Calculate the second sum: sum over n=1 to N of (2n / 2n+1)
    for n in range(1, N+1):
        sum2 += 2*n / (2*n + 1)
    
    return sum1 + sum2

# Define the value of N
N = 100

# Calculate S(2) for the given N
S2 = calculate_S2(N)

print(f"The value of S(2) for N = {N} is: {S2}")

#################################################

def calculate_S3(N):
    result = 0.0
    for n in range(1, N+1):
        result += 1 / (2*n*(2*n+1))
    return result

# Define the value of N
N = 100

# Calculate S(3) for the given N
S3 = calculate_S3(N)

print(f"The value of S(3) for N = {N} is: {S3}")


