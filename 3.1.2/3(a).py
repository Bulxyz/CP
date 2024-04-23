def calculate_S_UP(N):
    S_UP = 0.0
    for n in range(1, N+1):
        S_UP += 1 / n
    return S_UP

def calculate_S_DOWN(N):
    S_DOWN = 0.0
    for n in range(N, 0, -1):
        S_DOWN += 1 / n
    return S_DOWN

# Input the value of N
N = int(input("Enter the value of N: "))

# Calculate S_UP and S_DOWN
result_S_UP = calculate_S_UP(N)
result_S_DOWN = calculate_S_DOWN(N)

# Output the results
print(f"S_UP for N = {N}: {result_S_UP}")
print(f"S_DOWN for N = {N}: {result_S_DOWN}")
