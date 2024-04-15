import sys

underflow_limit = sys.float_info.min * 2
overflow_limit = sys.float_info.max / 2

print("Underflow limit (within a factor of 2):", underflow_limit)
print("Overflow limit (within a factor of 2):", overflow_limit)
