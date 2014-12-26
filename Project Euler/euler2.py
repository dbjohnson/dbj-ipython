#! /usr/bin/python

fib1 = 1
fib2 = 2
sum = 2

while (fib1 + fib2) <= 4000000:
	tmp = fib1 + fib2
	if (tmp % 2 == 0):
		sum += tmp
		
	fib1 = fib2
	fib2 = tmp

print sum