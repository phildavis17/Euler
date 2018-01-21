# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import primes

def is_triplet(a, b, c):
    if (a**2 + b**2) == c**2:
        return True
    else:
        return False

def searcher(max):
    for a in range(1, max + 1):
        for b in range(1, max - a):
            if is_triplet(a, b, max-a-b):
                return [a, b, max-a-b]

print(primes.list_product(searcher(1000)))
