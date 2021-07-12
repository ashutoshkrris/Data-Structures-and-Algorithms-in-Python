# Find the nth number in Fibonacci Series

def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer."
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
print(fibonacci(-6))
