
1.Underflow: Integers in Python do not have a predefined underflow limit like floating-point numbers. However, as the integers are represented using a variable number of bits, they can grow to very large negative values (limited by memory) before reaching an underflow condition.




2.Overflow: Integers in Python can grow to very large positive values before reaching an overflow condition. The upper limit for integers in Python 3 is determined by available memory, but theoretically, it can be as large as (231 - 1) or (263 - 1) based on whether it's a 32-bit or 64-bit Python build respectively.
