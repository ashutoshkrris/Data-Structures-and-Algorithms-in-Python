# Write a recursive function called someRecursive which accepts an array and a callback. The function returns true if a single value in the array returns true when passed to the callback. Otherwise it returns false.

def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def some_recursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return some_recursive(arr[1:], cb)
    return True


print(some_recursive([1, 2, 3, 4], is_odd))
print(some_recursive([4, 6, 8, 9], is_odd))
print(some_recursive([2, 4, 6, 8], is_odd))
