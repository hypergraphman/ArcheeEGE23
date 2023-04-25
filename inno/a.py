def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-f(n-1)) + f(n-f(n-2))


def g(n):
    return f(n) % 4


for i in range(1, 35):
    print(g(i))