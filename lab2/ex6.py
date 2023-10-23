# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.
def ex6(number, *lists):
    finalList = []
    freq = {}
    for lst in lists:
        for element in lst:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1
    for element in freq:
        if freq[element] == number:
            finalList.append(element)
    return finalList


result = ex6(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
print(result)
