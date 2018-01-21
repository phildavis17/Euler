# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

def triangle_num(n):
    return sum(list(range(1, n+1)))

coinvals = (1, 2, 5, 10, 20, 50, 100, 200)
combinations = {1:1}

def useful_coins(n, cl):
    return list(filter(lambda x: x < n, cl))

for c in coinvals:
    if c in combinations:
        continue
    combinations[c] = triangle_num(c)

print(combinations)



print(triangle_num(2))
print(useful_coins(20, coinvals))
