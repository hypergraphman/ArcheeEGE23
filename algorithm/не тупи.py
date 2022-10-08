from string import digits, ascii_uppercase


def n_to_p(n, p):
    r = ''
    d = digits + ascii_uppercase
    while n != 0:
        t = n % p
        r = d[t] + r
        n //= p
    return r


print(n_to_p(194, 5))
