def compare(dict1, dict2):
    # ambele s dictionare
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    # lungime la fel
    if len(dict1) != len(dict2):
        return False

    for key, value in dict1.items():
        # daca sunt aceleasi chei in ambele dict
        if key not in dict2:
            return False

        value2 = dict2[key]

        # verif daca mai contin alte dictionare, daca da, apelam recursiv
        if isinstance(value, dict) and isinstance(value2, dict):

            if not compare(value, value2):
                return False
        else:
            # daca nu s dict, le comparam direct
            if value != value2:
                return False
    return True


dict1 = {'a': 1, 'b': [1, 2, 5], 'c': {'x': 5, 'y': 6}}
dict2 = {'a': 1, 'b': [1, 2, 3], 'c': {'x': 5, 'y': 6}}

result = compare(dict1, dict2)
print(result)
