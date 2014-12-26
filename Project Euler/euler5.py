#! /usr/bin/python
import time

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

start = time.time()

maxDivisor = 20
divisors = range(maxDivisor, 1, -1)
n = maxDivisor
winner = 0
while True:
	foundIt = True
	for divisor in divisors:
		if (n % divisor) != 0:
			foundIt = False
			break

	if foundIt:
		winner = n
		break;
		
	n += maxDivisor
			
				
			
print 'Smallest value: ', winner
print 'Elapsed time: %1.2es' % (time.time() - start)
