# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple
def sortKey(lst):
        if len(lst) >= 2 and len(lst[1]) >= 3:
            return lst[1][2]
        else:
            return ''

def ex11(tuples):
    sorted_tuples = sorted(tuples, key=sortKey)
    return sorted_tuples


print(ex11([('abc', 'bcd'), ('abc', 'zza')]))
