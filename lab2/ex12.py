# Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters. Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

def ex12(listOfWords):
    listOfLists = []

    for word in listOfWords:
        exists = False

        for lst in listOfLists:
            if lst and word[-2:] == lst[0][-2:]:
                lst.append(word)
                exists = True

        if not exists:
            listOfLists.append([word])

    return listOfLists
print(ex12(['ana', 'banana', 'carte', 'arme', 'parte']))
