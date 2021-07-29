def capitalize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalize_first(arr[1:])


print(capitalize_first(['cat', 'Dog', 'boY']))
