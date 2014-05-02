#Project Euler Problem 1 @ http://projecteuler.net/problem=5
#By Michael H. / Aonbyte @ http://github.com/aonbyte
#Problem 5:
#
#2520 is the smallest number that can be divided by each of the numbers from 1
#to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the
#numbers from 1 to 20?

numberList = range(1,21)
foundNumber = False
newList = []
currentNumber = 0

while not foundNumber:
    currentNumber = currentNumber + 1
    for number in numberList:
        newList.append(currentNumber % number)
    if(all(element is True for element in newList)):
        foundNumber = True
    else:
        newList = []

#My solution takes forever but it gets there haha
#I wouldn't suggest running this unless you wanna come back in an hour
#I need to come back to this and make a better algorithm
#Solution is 232792560
