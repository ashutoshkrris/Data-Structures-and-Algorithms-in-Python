# Find factorial of n

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer."
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


print(factorial(5))
print(factorial(-5))
