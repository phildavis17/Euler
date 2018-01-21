# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

import primes

def string_cycles(s):
    varient = ''
    for i in range(len(s)):
        varient = s[i:] + s[0:i]
        yield varient

def cycles_are_prime(n):
    for v in string_cycles(str(n)):
        if not primes.is_prime(int(v)):
            return False
    return True

count = 1
lim = 1000000

for n in range(3, lim, 2):
    if primes.is_prime(n):
        if cycles_are_prime(n):
            count += 1

print(count)
