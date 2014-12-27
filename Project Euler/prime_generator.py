import math


def generate_primes(n):
	segment_length = 2**32
	segment_start = 0
	primes = []
	while segment_start < n:
		segment_end = min(n, segment_start + segment_length - 1)
		primes.extend(generate_primes_segment(segment_start, segment_end))
		segment_start += segment_length
	return primes


def generate_primes_segment(segment_start, segment_end):
	# print 'this is not nearly as efficient as it could be - fix it, Johnson
	if segment_end <= 1:
		return []

	segment_start = max(segment_start, 2)
	# sieve of Erotosthenes
	# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	segment_length = segment_end - segment_start + 1
	sieve = [1] * segment_length

	p = 2
	while p <= segment_end/2:
		m = max(int(math.ceil(float(segment_start) / p)), 2) * p

		while m <= segment_end:
			sieve[m-segment_start] = 0
			m += p

		p += 1
		# can't do this optimization with segmented approach
		# while p <= segment_end/2:
		# 	m = max(int(math.ceil(float(segment_start) / p)), 2) * p
		# 	if sieve[m-segment_start] == 0:
		# 		p += 1
		# 	else:
		# 		break

	primes = [i + segment_start for i, x in enumerate(sieve) if x != 0]
	return primes


def generate_primes_bitmask(n):
	if n <= 1:
		return []

	# sieve of Erotosthenes
	# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	bucket_width = 64
	nbuckets = int(round(float(n) / bucket_width + 0.5))
	full_bucket = (2**bucket_width) - 1
	sieve = [full_bucket] * nbuckets

	def p2bucket_bit(p):
		return (p / bucket_width, p % bucket_width)

	def set_bit(p):
		(bucket, bit) = (p / bucket_width, p % bucket_width)
		sieve[bucket] &= (1 << bit)

	def clear_bit(p):
		(bucket, bit) = (p / bucket_width, p % bucket_width)
		sieve[bucket] &= ~(1 << bit)

	def bit_is_set(p):
		(bucket, bit) = (p / bucket_width, p % bucket_width)
		return sieve[bucket] & (1 << bit) != 0

	clear_bit(0)
	clear_bit(1)

	p = 2
	while p <= n:
		m = 2*p
		all_removed = True
		while m <= n:
			if not all_removed or bit_is_set(m):
				all_removed = False
				clear_bit(m)
			m += p

		if all_removed:
			break

		p += 1
		while p <= n and not bit_is_set(p):
			p += 1

	primes = [p for p in xrange(n) if bit_is_set(p)]
	return primes


# x = 1000
# print generate_primes_bitmask(x)
# print generate_primes(x)
# print sorted(set(generate_primes(x)).symmetric_difference(set(generate_primes_bitmask(x))))
# from timeit import timeit
# # x = 3000
# # x = 76576500
# x = 765765
# print timeit(lambda: generate_primes_bitmask(x), number=1)
# print timeit(lambda: generate_primes(x), number=1)
# print timeit(lambda: generate_primes_segment(0, x), number=1)
