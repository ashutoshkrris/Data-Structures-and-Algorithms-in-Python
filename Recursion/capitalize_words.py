def capitalize_words(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalize_words(arr[1:])


print(capitalize_words(["i", "am", "learning", "recursion"]))
