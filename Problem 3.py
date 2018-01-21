# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


import math

def factors(n):
    f = []
    for k in range(2, int(math.sqrt(n))+1):
        if n % k == 0:
            f.append(k)
            if not n/k == k:
                f.append(int(n/k))
    return sorted(f)

def is_prime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def unique_prime_factors(n):
    pf = []
    for f in factors(n):
        if is_prime(f):
            pf.append(f)
    return pf

#print(factors(12))
print(is_prime(2000000))
#print(unique_prime_factors(600851475143))
