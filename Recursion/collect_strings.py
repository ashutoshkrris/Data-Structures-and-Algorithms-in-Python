# Write a function called collectStrings which accepts an object and returns an array of all the values in the object that have a typeof string.

def collect_strings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        if type(obj[key]) is dict:
            result = result + collect_strings(obj[key])

    return result

obj1 = {
    "stuff": "foo",
    "bar": 1,
    "data": {
        "random": "Hello",
        "what": 1
    }
}

print(collect_strings(obj1))