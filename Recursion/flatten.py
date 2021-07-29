# Write a recursive function called flatten which accepts an array and returns new array with all values flattened

def flatten(arr):
    result = []
    for item in arr:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


print(flatten([1, 2, 3, [4, 5]]))
print(flatten([1, [2, [3, 4], [[5]]]]))
print(flatten([[1], [2], [3]]))
print(flatten([[[1], [[[2]]], [[[3]]]]]))
