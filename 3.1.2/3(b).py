import math
import matplotlib.pyplot as plt

def calculate_S_UP(N):
    S_UP = sum(1/n for n in range(1, N+1))
    return S_UP

def calculate_S_DOWN(N):
    S_DOWN = sum(1/n for n in range(N, 0, -1))
    return S_DOWN

# Calculate the values of the expression for different N
N_values = list(range(1, 1001))  # N values from 1 to 1000
result_values = []

for N in N_values:
    S_UP = calculate_S_UP(N)
    S_DOWN = calculate_S_DOWN(N)
    
    denominator = abs(S_UP) + abs(S_DOWN)
    result = (S_UP - S_DOWN) / denominator if denominator != 0 else 0  # Handle division by zero
    
    result_values.append(result)

# Create a log-log plot
plt.figure()
plt.plot(N_values, result_values, label='(S(up) - S(down)) / (|S(up)| + |S(down)|)')
plt.xlabel('N')
plt.ylabel('(S(up) - S(down)) / (|S(up)| + |S(down)|)')
plt.title('Plot of Expression vs. N')
plt.legend()
plt.grid(True)
plt.show()
