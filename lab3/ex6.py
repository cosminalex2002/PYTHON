def count(input):
    uniqueElem = set()
    duplicates = set()

    for element in input:
        if element in uniqueElem:
            duplicates.add(element)
        else:
            uniqueElem.add(element)

    countUniq = len(uniqueElem)
    countDuplicates = len(duplicates)

    return countUniq, countDuplicates


input = [1, 2, 3, 2, 4, 3, 5, 6, 5]
result = count(input)
print(result)
