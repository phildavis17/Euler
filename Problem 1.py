# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_multiples(n, lim):
    if n > lim:
        return 0
    total = 0
    current = n
    while current < lim:
        total += current
        current += n
    return total

three = sum_of_multiples(3, 1000)
five = sum_of_multiples(5, 1000)
fifteen = sum_of_multiples(15, 1000)

answer = three + five - fifteen

print(answer)
