from decimal import Decimal, getcontext
import math

def sin_series_terms_restricted(x, N):
    series_terms = []
    for n in range(1, N+1):
        term = (-1)**(n-1) *Decimal(x)**(2*n-1) / math.factorial(2*n-1)
        series_terms.append(term)
    
    return series_terms

def adjust_x_to_range(x):
    two_pi = Decimal(2) * Decimal(math.pi)
    while x > Decimal(math.pi):
        x -= two_pi
    while x < 0:
        x += two_pi
    return x

x = Decimal(3) * Decimal(math.pi)  # Value of x (approximately 3π)
x = adjust_x_to_range(x)  # Adjust x to be within the range 0 ≤ x ≤ π
N = 100  # Number of terms in the series

# Set the precision for Decimal calculations
getcontext().prec = 50

series_terms = sin_series_terms_restricted(x, N)

n_cancelation = int(x / 2)  # Index around n ≈ x/2 for cancelation observation

print(f"Terms in the series for x in the range 0 ≤ x ≤ π:")
for n, term in enumerate(series_terms):
    if n == n_cancelation:
        print(f"Near-perfect cancelation around n ≈ x/2 at term {n}: {term}")
    else:
        print(f"Term {n}: {term}")
