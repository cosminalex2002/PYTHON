def operations(*args):
    result = {}

    for i in range(len(args)):
        for j in range(i+1, len(args)):
            set1 = args[i]
            set2 = args[j]

            result[f"{set1} | {set2}"] = set1 | set2
            result[f"{set1} & {set2}"] = set1 & set2
            result[f"{set1} - {set2}"] = set1 - set2
            result[f"{set2} - {set1}"] = set2 - set1

    return result

set1 = {1, 2}
set2 = {2, 3}

result_dict = operations(set1, set2)
print(result_dict)
