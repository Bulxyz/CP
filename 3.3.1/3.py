from decimal import Decimal, getcontext
import math

def sin_series_terms(x, N):
    series_terms = []
    for n in range(1, N+1):
        term = (-1)**(n-1) *Decimal(x)**(2*n-1) / math.factorial(2*n-1)
        series_terms.append(term)
    
    return series_terms

x = Decimal(3) * Decimal(math.pi)  # Value of x (approximately 3π)
N = 100  # Number of terms in the series

# Set the precision for Decimal calculations
getcontext().prec = 50

series_terms = sin_series_terms(x, N)

n_cancelation = int(x / 2)  # Index around n ≈ x/2 for cancelation observation

print(f"Terms in the series for x ≈ 3π:")
for n, term in enumerate(series_terms):
    if n == n_cancelation:
        print(f"Near-perfect cancelation around n ≈ x/2 at term {n}: {term}")
    else:
        print(f"Term {n}: {term}")
