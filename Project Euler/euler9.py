# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# <codecell>

import math

foundit = False
for a in xrange(1, 1000/3):
    for b in xrange(a+1, (1000-a)/2):
        cc = a*a + b*b
        c = int(math.sqrt(a*a + b*b))
        if c*c == cc and a+b+c == 1000:
            print 'a, b, c: [%d, %d, %d]  prod: %d' % (a, b, c, a*b*c)
            foundit = True
            break
    if foundit:
        break
else:
    print "Couldn't find it!"

