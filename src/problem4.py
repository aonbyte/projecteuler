#Project Euler Problem 1 @ http://projecteuler.net/problem=4
#By Michael H. / Aonbyte @ http://github.com/aonbyte
#Problem 4:
#
#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    """Returns whether or not a number is a palindrome"""
    string = str(number)
    return string == string[::-1]

firstDigitList = range(100,1000)
secondDigitList = range(100,1000)
possiblePalindrome = 0
finalFirstDigit = 0
finalSecondDigit = 0



for digit in firstDigitList:
    first = digit
    for digit in secondDigitList:
        second = digit
        if isPalindrome(first * second) and (first * second) > possiblePalindrome:
            possiblePalindrome = first * second
            finalFirstDigit = first
            finalSecondDigit = second

print 'Largest First Digit is: ' + str(finalFirstDigit)
print 'Largest Second Digit is: ' + str(finalSecondDigit)
print 'The Palindrome of those products is: ' + str(possiblePalindrome)
#Solution is 906609
