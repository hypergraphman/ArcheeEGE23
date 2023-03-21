from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 5:
        return 2 * n
    if n > 5 and n % 2 == 0:
        return f(n - 2) + 3 * f(n // 2) + n
    if n > 5 and n % 2 != 0:
        return f(n - 1) + f(n - 2) + f(n - 3)


for i in range(1, 4000):
    f(i)
print(f(99) + f(4000))