# Convert a number from decimal to binary.

def decimal_to_binary(number):
    assert int(number) == number, "The number must be an integer."
    if number == 0:
        return 0
    return number % 2 + 10 * decimal_to_binary(int(number/2))


print(decimal_to_binary(12))
print(decimal_to_binary(-12))
print(decimal_to_binary(1.2))
