# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

def fib(lim):
    f = [0,1]
    total = 0
    while True:
        n = f[-2] + f[-1]
        if n > lim:
            return f
        else:
            f.append(n)

l = fib(4000000)

k = 0
total = 0
while k < len(l):
    total += l[k]
    k += 3

print(total)
