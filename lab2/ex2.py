
# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2) + 1):
        if (n % i) == 0:
            return False
    return True


def listOfPrimes(list):
    listPrimes = []
    for i in list:
        if (isPrime(i)):
            listPrimes.append(i)
    return listPrimes

numbers = [2, 3, 5, 7, 10, 15, 20, 23, 29]
print(listOfPrimes(numbers))
