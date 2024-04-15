import math

def good_way_sum(x, eps=1e-8):
    term = x
    sum_val = x
    n = 1
    while abs(term / sum_val) > eps:
        term = -term *x* x / ((2 *n + 1)* (2 * n - 2))
        sum_val += term
        n += 1
    return sum_val

def bad_way_sum(x, eps=1e-8):
    term = x
    sum_val = x
    factorial = 1
    n = 1
    while abs(term / sum_val) > eps:
        factorial *= (2* n + 1) *(2* n - 2)
        term = -term *x* x / factorial
        sum_val += term
        n += 1
    return sum_val

# Calculate the series for different x values
x_values = [0.1, 0.5, 1.0]
print("x \t imax \t sum \t |sum - sin(x)| / sin(x)")

for x in x_values:
    sum_good = good_way_sum(x)
    sum_bad = bad_way_sum(x)
    sin_x = math.sin(x)
    relative_error_good = abs((sum_good - sin_x) / sin_x)
    relative_error_bad = abs((sum_bad - sin_x) / sin_x)
    print(f"{x} \t {len(range(1, 1000))} \t {sum_good} \t {relative_error_good}")
