# Find GCD of two numbers.

def gcd(x, y):
    assert int(x) == x and int(y) == y, "The numbers must be integers."
    if x < 0:
        x = -1*x
    if y < 0:
        y = -1*y
    if y == 0:
        return x
    return gcd(y, x % y)


print(gcd(18, 48))
print(gcd(18, 0))
print(gcd(0, 0))
print(gcd(0, 18))
print(gcd(-4, 18))
print(gcd(-4, 1.8))
