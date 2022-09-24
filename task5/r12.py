from itertools import permutations


def alg(n):
    pairs = set()
    for d1, d0 in permutations(str(n), r=2):
        num = int(d1 + d0)
        if 10 <= num <= 99:
            pairs.add(num)
    return max(pairs) - min(pairs)


i = 100
while alg(i) != 40:
    i += 1
print(i)
