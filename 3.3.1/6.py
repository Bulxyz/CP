import matplotlib.pyplot as plt
from decimal import Decimal, getcontext
import math

def sin_series_terms_restricted(x, N):
    series_terms = []
    for n in range(1, N+1):
        term = (-1)**(n-1) *Decimal(x)**(2*n-1) / math.factorial(2*n-1)
        series_terms.append(term)
    
    return series_terms

def calculate_sin_approximation(x, N):
    series_terms = sin_series_terms_restricted(x, N)
    sin_approximation = sum(series_terms)
    return sin_approximation

# Set the precision for Decimal calculations
getcontext().prec = 50

x_values = [1, 5, 10, 15, 20]  # Values of x for plotting
N_values = range(1, 101)  # Range of N values

for x in x_values:
    errors = []
    for N in N_values:
        x_decimal = Decimal(x)
        sin_approximation = calculate_sin_approximation(x_decimal, N)
        sin_actual = Decimal(math.sin(x_decimal))

        error = abs(sin_actual - sin_approximation)
        errors.append(error)

    plt.plot(list(N_values), errors, label=f'x = {x}')

plt.xlabel('Number of Terms (N)')
plt.ylabel('Error')
plt.title('Error vs. Number of Terms for Different Values of x')
plt.legend()
plt.grid(True)
plt.show()
