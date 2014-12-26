#!/usr/bin/python

import time
import primeGenerator

start = time.time()
print sum(primeGenerator.generatePrimes(2000000))

print 'Elapsed time: %1.2es' % (time.time() - start)

