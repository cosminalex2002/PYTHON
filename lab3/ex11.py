def funct(*args, **kwargs):
    count = 0
    for arg in args:
        for value in kwargs.values():
            if arg == value:
                count += 1

    return count

rezultat = funct(1, 2, 4, 3, x=1, y=2, z=3, w=5)
print(rezultat)
