#! /usr/bin/python

import math

def generatePrimes(n):
	segmentLength = 2**32
	segmentStart = 0
	primes = []
	while segmentStart < n:
		segmentEnd = min(n, segmentStart + segmentLength - 1)
		primes.extend(generatePrimesSegment(segmentStart, segmentEnd))
		segmentStart += segmentLength
	return primes

def generatePrimesSegment(segmentStart, segmentEnd):
	print 'this is not nearly as efficient as it could be - fix it, Johnson'
	if segmentEnd <= 1:
		return []
		
	segmentStart = max(segmentStart, 2)
	# sieve of Erotosthenes
	# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	
	segmentLength = segmentEnd - segmentStart + 1
	sieve = [1] * segmentLength

	p = 2
	while p <= segmentEnd/2:
		m = max(int(math.ceil(float(segmentStart) / p)), 2) * p

		while m <= segmentEnd:
			sieve[m-segmentStart] = 0
			m += p
		
		p += 1
		# can't do this optimization with segmented approach
		# while p <= segmentEnd/2:
		# 	m = max(int(math.ceil(float(segmentStart) / p)), 2) * p
		# 	if sieve[m-segmentStart] == 0:
		# 		p += 1
		# 	else:
		# 		break

			
	
	primes = [i + segmentStart for i, x in enumerate(sieve) if x != 0] 
	return primes


def generatePrimesBitmask(n):
	if n <= 1:
		return []
		
	# sieve of Erotosthenes
	# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	bucketWidth = 64
	nbuckets = int(round(float(n) / bucketWidth + 0.5))
	fullBucket = (2**bucketWidth) - 1
	sieve = [fullBucket] * nbuckets

	def p2bucketBit(p):
		return (p / bucketWidth, p % bucketWidth)

	def setBit(p):
		(bucket, bit) = (p / bucketWidth, p % bucketWidth)
		sieve[bucket] &= (1 << bit)

	def clearBit(p):
		(bucket, bit) = (p / bucketWidth, p % bucketWidth)
		sieve[bucket] &= ~(1 << bit)

	def bitIsSet(p):
		(bucket, bit) = (p / bucketWidth, p % bucketWidth)
		return sieve[bucket] & (1 << bit) != 0


	clearBit(0)
	clearBit(1)

	p = 2
	while p <= n:
		m = 2*p
		allRemoved = True
		while m <= n:
			if not allRemoved or bitIsSet(m):
				allRemoved = False
				clearBit(m)
			m += p
		
		if allRemoved:
			break
		
		p += 1
		while p <= n and not bitIsSet(p):
			p += 1
			
	
	primes = [p for p in xrange(n) if bitIsSet(p)] 
	return primes


x = 1000
print generatePrimesBitmask(x)
print generatePrimes(x)
print sorted(set(generatePrimes(x)).symmetric_difference(set(generatePrimesBitmask(x))))
from timeit import timeit
# x = 3000
# x = 76576500
x = 765765
print timeit(lambda: generatePrimesBitmask(x), number=1)
print timeit(lambda: generatePrimes(x), number=1)
print timeit(lambda: generatePrimesSegment(0, x), number=1)
