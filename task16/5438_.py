from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    if n != 1:
        return f(n-1) * 3**((n%5)-(n%7))


for i in range(2000):
    f(i)


print(f(2000) / f(1995))
