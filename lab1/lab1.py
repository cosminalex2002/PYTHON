# 1. Find The greatest common divisor of multiple numbers read from the console.
# def cmmdc(a, b):
#     if(b == 0):
#         return a
#     else:
#         return cmmdc(b, a % b)
#
# def ex1():
#     inputStr = input("Numbers: ")
#     numbersString = inputStr.split()
#     numbers = [int(n) for n in numbersString]
#     if len(numbers) == 0:
#         return None
#     elif len(numbers) == 1:
#         return numbers[0]
#     else:
#         cmmdcNumber = cmmdc(numbers[0] ,numbers[1])
#         for num in numbers[2:]:
#             cmmdcNumber = cmmdc(cmmdcNumber, num)
#     return cmmdcNumber
#
# print(ex1())


# 2. Write a script that calculates how many vowels are in a string.

# def ex2(string):
#     counter = 0
#     vowels = "AEIOUaeiou"
#     for char in string:
#         if char in vowels:
#             counter += 1
#     return counter
#
#
# print(ex2("ana are mere"))

# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

# def ex3(string1, string2):
#     counter = string2.count(string1)
#     return counter
#
# string1 = input("string1: ")
# string2 = input("string2: ")
#
# print(ex3(string1, string2))

# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

# def ex4(text):
#     if text[0].isupper():
#         text = text[0].lower() + text[1:]
#
#     result = ""
#     for char in text:
#         if char.isupper():
#             result += "_" + char.lower()
#         else:
#             result += char
#     return result
#
# print(ex4("UpperCamelCase"))


# 5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
# def spiral(matrix):
#     top = 0
#     bottom = len(matrix) - 1
#     left = 0
#     right = len(matrix[0]) - 1
#     result = []
#     while top <= bottom and left <= right:
#         for i in range(left, right + 1):
#             result.append(matrix[top][i])
#         top += 1
#         for i in range(top, bottom + 1):
#             result.append(matrix[i][right])
#         right -= 1
#         if top <= bottom and left <= right:
#             for i in range(right, left - 1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -= 1
#             for i in range(bottom, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1
#     return result
#
# matrix = [
#     ['a', 'b', 'c', 'd'],
#     ['l', 'm', 'n', 'e'],
#     ['k', 'p', 'o', 'f'],
#     ['j', 'i', 'h', 'g']
# ]
#
# print(spiral(matrix))

# 6.Write a function that validates if a number is a palindrome.
# def ex6(number):
#     copyNumber = number
#     reversedNumber = 0
#
#     while number > 0:
#         reversedNumber = reversedNumber * 10 + number % 10
#         number = number // 10
#
#     return copyNumber == reversedNumber
#
# number = 12321
# if ex6(number):
#     print("yes")
# else:
#     print("no")


# 7.Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.
# def ex7(text):
#     ok = False
#     result = ""
#
#     for char in text:
#         if char.isdigit():
#             result += char
#             ok = True
#         elif ok:
#             break
#
#     return result
#
# text1 = "An apple is 123 USD"
# text2 = "abc123abc"
# print(ex7(text1))
# print(ex7(text2))


# 8.Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
# def ex8(number):
#     count = 0
#     while number:
#         if number & 1 == 1:
#             count += 1
#         number = number // 2
#
#     return count
# print(ex8(24))



# 9.Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

# def ex9(text):
#     chars = {}
#     maxFreq = 0
#     mostFreqChar = ''
#
#     for char in text:
#         if char.isalpha():
#             if char in chars:
#                 chars[char] += 1
#             else:
#                 chars[char] = 1
#
#             if chars[char] > maxFreq:
#                 maxFreq = chars[char]
#                 mostFreqChar = char
#
#     return mostFreqChar
#
# print(ex9("an apple is not a tomato"))


# 10.Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.
def ex10(text):
    count = 0
    for i in range(len(text)):
        if i == 0 and text[i] != ' ':
            count += 1
        elif text[i] != ' ' and text[i - 1] == ' ':
            count += 1

    return count

print(ex10("I have Python exam"))
