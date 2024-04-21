import math

# Function to calculate the sum using the "bad way" method with explicit factorials
def bad_way_sum(x, max_iter=1000, eps=1e-8):
    term = x
    sum_val = x
    n = 2  # Start n from 2 to avoid division by zero
    for _ in range(max_iter):
        term = -term *x* x / ((2 *n + 1)* (2 * n - 2))  # Calculate the next term in the series with explicit factorials
        sum_val += term  # Add the term to the sum
        if abs(term / sum_val) < eps:
            return sum_val, n  # Return the sum value and the final n value
        n += 1  # Increment the iteration count
    return None, None  # Return None if convergence is not achieved within max_iter

# Define x values for testing convergence with increasing x
x_values = [10000, 100000, 1000000, 10000000]

# Print table headings
print("x\timax\tsum\t|sum - sin(x)|/sin(x)")

# Calculate and print results for each x value
for x in x_values:
    sin_x = math.sin(x)
    sum_bad, n = bad_way_sum(x)  # Retrieve the sum value and the final n value
    if sum_bad is not None:
        relative_error = abs(sum_bad - sin_x) / sin_x
        print(f"{x}\t{n}\t{sum_bad}\t{relative_error}")
    else:
        print(f"{x}\tNot Converged\tN/A\tN/A")
