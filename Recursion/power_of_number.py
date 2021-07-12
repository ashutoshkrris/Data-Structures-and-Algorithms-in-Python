# Calculate the power of a number.

def power_of_number(base, exponent):
    assert exponent >= 0 and int(exponent) == exponent, "The exponent must be a positive integer."
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if base == 0:
        return 0
    return base*power_of_number(base, exponent-1)


print(power_of_number(2, 4))
print(power_of_number(-2, 4))
print(power_of_number(2.4, 4))
print(power_of_number(2, 4.3))
print(power_of_number(2, -4))
print(power_of_number(-2, -4))
