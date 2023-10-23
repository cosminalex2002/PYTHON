# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def intersection(listA, listB):
    listC = [value for value in listA if value in listB]
    return listC

def union(listA, listB):
    listC = []
    listC.extend(listA)
    for i in listB:
        if i not in listC:
            listC.append(i)
    return listC
def A_B(listA,listB):
    listC=[value for value in listA if value not in listB]
    return listC
def B_A(listA,listB):
    listC=[value for value in listB if value not in listA]
    return listC

listA = [1, 2, 3, 4, 5, 6]
listB = [2, 4, 6, 8, 10, 12]
print(intersection(listA,listB))
print(union(listA,listB))
print(A_B(listA,listB))
print(B_A(listA,listB))

