#Project Euler Problem 1 @ http://projecteuler.net/problem=2
#By Michael H. / Aonbyte @ http://github.com/aonbyte
#Problem 2:
#
#Each new term in the Fibonacci sequence is generated by adding the previous
#two terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#By considering the terms in the Fibonacci sequence whose values do not exceed
#four million, find the sum of the even-valued terms.

def fib(n):
    """Returns the nth term in the fibonacci sequence"""
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

maximumValue = 4000000
i = 0
listOfEvenTerms = []

while fib(i) < maximumValue:
    currentTerm = fib(i)
    if currentTerm % 2 is 0:
        listOfEvenTerms.append(currentTerm)
    i = i + 1


sumOfEvenTerms = sum(listOfEvenTerms)
print sumOfEvenTerms
#Solution is 4613732
