#Project Euler Problem 1 @ http://projecteuler.net/problem=3
#By Michael H. / Aonbyte @ http://github.com/aonbyte
#Problem 3:
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143?

number = 600851475143
i = 2

while i * i < number:
    while number % i == 0:
        number = number / i
    i = i + 1
print number
#Solution is 6857
