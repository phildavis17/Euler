# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural
# numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

def sum_of_n_squares(n):
    sum = 0
    for k in range(1, n+1):
        sum += k**2
    return sum

def square_of_n_sumes(n):
    square = 0
    for k in range(1, n+1):
        square += k
    return square**2

sm = sum_of_n_squares(100)
sq = square_of_n_sumes(100)

print(sm - sq)
