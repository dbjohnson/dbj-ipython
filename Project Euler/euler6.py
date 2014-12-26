#! /usr/bin/python
import time


# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

start = time.time()

n = 100

s = sum(xrange(1, n+1))
ssq = sum([x*x for x in xrange(1, n+1)])
diff = s*s - ssq

print 'Difference: ', diff
print 'Elapsed time: %1.2es' % (time.time() - start)
