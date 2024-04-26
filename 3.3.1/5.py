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

for x in range(1, 101):
    x_decimal = Decimal(x)
    N = 100  # Number of terms in the series
    sin_approximation = calculate_sin_approximation(x_decimal, N)
    sin_actual = Decimal(math.sin(x_decimal))

    error = abs(sin_actual - sin_approximation)
    if error > Decimal('0.1'):
        print(f"At x = {x}: Series starts to lose accuracy. Error: {error}")
    if error > Decimal('1'):
        print(f"At x = {x}: Series no longer converges. Error: {error}")
