def ex8(number=1, listStrings=[], flag=True):
    finalList = []

    for string in listStrings:
        sublist = []

        for char in string:
            if (ord(char) % number == 0) == flag:
                sublist.append(char)

        finalList.append(sublist)

    return finalList

x = 2
strings = ["test", "hello", "lab002"]
flag = False
print(ex8(x, strings, flag))
