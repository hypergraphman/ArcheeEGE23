def f(s, k):
    if s == 80 and k <= 5:
        return 1
    if s > 80 or k > 5:
        return 0
    return f(s + 1, k + 1) + f(s * 2, k + 1) + f(s + s % 4, k + 1)


amount = 0
for n in range(1, 80 + 1):
    if f(n, 0):
        amount += 1
print(amount)


def f(a, c, nach):
    if a == 80 and c <= 5:
        C.add(nach)
        return
    if a > 80 or c > 5:
        return
    c += 1
    return f(a + 1, c, nach), f(a * 2, c, nach), f(a + (a % 4), c, nach)
C = set()
for i in range(1, 82):
    f(i, 0, i)
print(C, len(C))