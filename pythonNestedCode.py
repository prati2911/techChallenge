# We have a nested object, we would like a function that you pass in the object and a key and get back the value. How this is implemented is up to you.
##
# Example Inputs
# object = {“a”:{“b”:{“c”:”d”}}}
# key = a/b/c
##
# object = {“x”:{“y”:{“z”:”a”}}}
# key = x/y/z
# value = a

def getKey(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('Empty Dictionary or Multiple Keys Found')
    else:
        return keys[0]


def getNestedValue(obj: dict, key: str, isFound = False):
    # print(obj, key, isFound)
    if type(obj) is not dict and not isFound:
        return None
    if (isFound or (key in obj.keys())) :
        if type(obj[key]) is dict:
            return getNestedValue(obj[key], getKey(obj[key]), True)
        else:
            # print(f'obj[getKey(obj)]: {obj[getKey(obj)]}')
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getNestedValue(obj[nestedKey], key, False)

if __name__ == '__main__':
    obj = {'x': {'y': {'z': 'a'}}}
    value = getNestedValue(obj, 'z')
    print("Final Value of the Code is:",value)