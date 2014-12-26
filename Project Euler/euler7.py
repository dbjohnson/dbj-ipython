#! /usr/bin/python
import time
import primeGenerator

# What is the 10 001st prime number?

start = time.time()

print primeGenerator.generatePrimes(int(1e6))[10000]

print 'Elapsed time: %1.2es' % (time.time() - start)
