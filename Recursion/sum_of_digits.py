# Find sum of digits of a positive integer.

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer."
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)


print(sum_of_digits(12345))
print(sum_of_digits(-12345))