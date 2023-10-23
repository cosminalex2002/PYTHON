# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def palindrome(number):
    copyNumber = number
    reversedNumber = 0

    while number > 0:
        reversedNumber = reversedNumber * 10 + number % 10
        number = number // 10

    return copyNumber == reversedNumber


def ex7(listNumbers):
    counter = 0
    max = 0;
    for num in listNumbers:
        if palindrome(num):
            counter += 1
            if num > max:
                max = num
    tuple = (counter, max)
    return tuple


numbers = [121, 1331, 12345, 12321, 45654, 78987]
result = ex7(numbers)
print("Număr de palindroame:", result[0])
print("Cel mai mare palindrom:", result[1])
