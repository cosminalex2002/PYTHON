# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Example: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.
def ex10(*lists):
    maxLen = max(len(lst) for lst in lists)
    result = []

    for i in range(maxLen):
        tupleList = []
        for lst in lists:
            if i < len(lst):
                tupleList.append(lst[i])
            else:
                tupleList.append(None)
        result.append(tuple(tupleList))

    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
print(ex10(list1, list2, list3))
