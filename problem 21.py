# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math
import primes as p

def extended_factors(n):
    f = []
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            yield k
            if not n/k == k:
                yield int(n/k)

def antipode(n):
    return sum(extended_factors(n), 1)

def is_amicable(n):
    if antipode(antipode(n))  == n and antipode(n) != n:
        return True
    return False

#print(antipode(220))
#print(antipode(284))

s = 0
# 1...?
for n in range(1, 10000):
    if is_amicable(n):
        print(n)
        s += n

print(s)
