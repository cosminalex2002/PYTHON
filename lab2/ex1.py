
#Write a function to return a list of the first n numbers in the Fibonacci string.
def fibb(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = [0, 1]
        while len(seq) < n:
            next = seq[-1] + seq[-2]
            seq.append(next)
        return seq

print(fibb(10))
