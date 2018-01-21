# A module created for use in solving Project Euler problems, many of which
# revolve around prime numbers.

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

def nth_prime(n):
    p = 1
    i = 1
    if n == 1:
        return 2
    while i < n:
        p += 2
        if is_prime(p):
            i += 1
    return p

def unique_prime_factors(n):
    pf = []
    for f in factors(n):
        if is_prime(f):
            pf.append(f)
    if not pf:
        return [n]
    return pf

def lowest_prime_factor(n):
    for f in factors(n):
        if is_prime(f):
            return f
    return n

def list_product(l):
    r = 1
    for i in l:
        r *= i
    return r

def is_squarefree(n):
    if list_product(unique_prime_factors(n)) == n:
        return True
    return False

def prime_factors(n):
    pf = []
    lpf = lowest_prime_factor(n)
    pf.append(lpf)
    if lpf == n:
        return pf
    pf.append(int(n/lpf))
    if is_prime(pf[-1]):
        return pf
    else:
        pf.extend(prime_factors(pf.pop()))
    return pf

def test():
    print('primes has been imported successfully')
