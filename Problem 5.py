# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

import primes

def is_subset(la, lb):
    sa = set(la)
    #sb = set(lb)

    for i in sa:
        if la.count(i) > lb.count(i):
            return False
    return True

def least_common_multiple(m = []):
    nums = []
    mpfs = []
    for n in m:
        nums.append(primes.prime_factors(n))
    # Build the list
    for g in nums:
        for f in set(g):
            while mpfs.count(f) < g.count(f):
                mpfs.append(f)
    return primes.list_product(mpfs)


p8 = primes.prime_factors(8)
p16 = primes.prime_factors(16)

print(least_common_multiple(list(range(1, 21))))
