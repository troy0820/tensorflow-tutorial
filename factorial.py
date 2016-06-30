#!/usr/bin/python
import sys

def factorial(number):
	if(number == 1):
		return number
	return number * factorial(number - 1)

if (len(sys.argv) > 1):
    x = int(sys.argv[1])
else:
    x = input('Enter a number for the factorial ')

y = factorial(x)

print('Factorial of 5 is {answer}'.format(answer=y))
