# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors
# each. What is the first of these numbers?


import primes as p

def distinct_prime_string(n):
    chain = 0
    test = 2
    while chain != n:
        a = len(p.unique_prime_factors(test))
        if a == n:
            chain = 1
            for m in range(test + 1, test + n):
                if len(p.unique_prime_factors(m)) == n:
                    chain += 1
        test += 1
    return test

print(distinct_prime_string(4)-1)
