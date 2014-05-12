#Project Euler Problem 1 @ http://projecteuler.net/problem=6
#By Michael H. / Aonbyte @ http://github.com/aonbyte
#Problem 6:
#
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural
#numbers and the square of the sum is 385 - 3025 = 2640
#
#Find the difference between the sum of the squares of the first one hundred
#natural numbers and the square of the sum.

def get_squares(inputList):
    """Takes a list of integers and returns a list of the elements squared"""
    return [element * element for element in inputList]

def get_sum(inputList):
    """Takes a list of integers and returns the sum of all elements in list"""
    return sum(inputList)

def sum_of_squares(inputList):
    """Takes a list of integers and returns the sum of the squares of integers"""
    return sum(get_squares(inputList))

numbers = range(1,101) #First one hundred natural numbers

sumSquares = sum_of_squares(numbers) #Sum of the squares of first 100 natural numbers

squareOfSum = get_sum(numbers) ** 2 #square of the sum of the first 100 natural numbers

difference = squareOfSum - sumSquares

print difference