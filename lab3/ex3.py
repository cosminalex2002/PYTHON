def compare(dict1, dict2):
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare(value1, value2):
                return False
        elif isinstance(value1, (list, set, tuple)) and isinstance(value2, (list, set, tuple)):
            if len(value1) != len(value2):
                return False
            for v1, v2 in zip(value1, value2):
                if v1 != v2:
                    return False
        else:
            if value1 != value2:
                return False
    return True

dict1 = {'a': 1, 'b': [1, 2, 5], 'c': {'x': 5, 'y': 6}}
dict2 = {'a': 1, 'b': [1, 2, 3], 'c': {'x': 5, 'y': 6}}
result = compare(dict1, dict2)
print(result)
