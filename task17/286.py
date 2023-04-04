def sum_oct(n):
    res = 0
    while n > 0:
        res += n % 8
        n //= 8
    return res


# sum(map(int, f'{n:o}'))
*a, = map(int, open('17-282.txt').read().split())
# min21 = 10**10
# for el in a:
#     if el % 21 == 0 and el < min21:
#         min21 = el
min21 = min(filter(lambda x: x % 21 == 0, a))
s_oct_min21 = sum(map(int, f'{min21:o}'))

res = []
# for i in range(len(a) - 1):
#     p1, p2 = a[i], a[i + 1]
for p1, p2 in zip(a, a[1:]):
    if sum(map(int, f'{p1:o}')) == s_oct_min21 or sum_oct(p2) == s_oct_min21:
        res.append(p1 + p2)
print(len(res), min(res))