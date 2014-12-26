#! /usr/bin/python
import time
import math


#Find the largest palindrome made from the product of two 3-digit numbers.

start = time.time()

def reverse(n):
     reversed = 0
     while n > 0:
          reversed = 10*reversed + n % 10
          n /= 10
     return reversed

largest = None
for i in xrange(100, 1000):
	for j in xrange(i, 1000):
		prod = i*j
		if prod > largest and prod == reverse(prod):
			largest = prod
			

			
print 'Largest palindrome: ', largest			
print 'Elapsed time: %1.2es' % (time.time() - start)

