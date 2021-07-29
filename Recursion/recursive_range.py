# Write a function called recursive_range which accepts a number and adds up all the numbers from 0 to the number passed to the function.

def recursive_range(num):
    if num <= 0:
        return 0
    return num + recursive_range(num-1)


print(recursive_range(6))
print(recursive_range(0))
print(recursive_range(-5))
