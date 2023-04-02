def f(s, e):
    if s == e:
        return 1
    if s > e or s == 25:
        return 0
    return f(s + 1, e) + f(s * 2, e)


print(f(2, 14) * f(14, 29))