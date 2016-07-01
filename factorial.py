#!/usr/bin/python
import sys

def factorial(number):
	if(number == 1):
		return number
	return number * factorial(number - 1)

def printstuff(message):
    print'This is the printed message: ' + message

if (len(sys.argv) > 1):
    x = int(sys.argv[1])
else:
    x = input('Enter a number for the factorial ')

y = factorial(x)

print('Factorial of {x} is {answer}'.format(x=x, answer=y))
