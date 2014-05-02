#Project Euler Problem 1 @ http://projecteuler.net/problem=1
#By Michael H. / Aonbyte @ http://github.com/aonbyte
#Problem 1:
#
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we
#get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
#multiples of 3 or 5 below 1000.

def multipleOfThree(number):
    """Returns whether or not the number is a multiple of three"""
    return (number % 3) is 0

def multipleOfFive(number):
    """Returns whether or not the number is a multiple of five"""
    return (number % 5) is 0

listOfNumbers = range(1000)
listOfMultiples = []

for number in listOfNumbers:
    if multipleOfThree(number) or multipleOfFive(number):
        listOfMultiples.append(number)

sumOfMultiples = sum(listOfMultiples)
print sumOfMultiples
#Solution is 233168
