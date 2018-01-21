# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def generate_palindromes(n):
    p = []
    u = int(math.ceil(n/2))
    d = int(math.floor(n/2))
    for x in range(10**(u-1), 10**u):
        a = str(x)
        for i in range(d-1, -1, -1):
            a += a[i]
        p.append(int(a))
    return(p)

#print(len(generate_palindromes(3)))

def three_digit_factors(n):
    for x in range(100, 1000):
        if n % x ==0 and len(str(int(n/x))) == 3:
            return True
    return False

scope5 = generate_palindromes(5)
scope6 = generate_palindromes(6)
scope = sorted(scope5 + scope6)
scope.reverse()

print(len(scope))


for g in scope:
    if three_digit_factors(g):
        print(g)
        break
print("uh oh!")
