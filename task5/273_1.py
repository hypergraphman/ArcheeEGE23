def alg(n):
    s1 = f'{n:b}'
    if n % 2:
        s2 = '1' + s1 + '0'
    else:
        s2 = '11' + s1 + '11'
    return int(s2, 2)


i = 10000
while alg(i) >= 126:
    i -= 1
print(alg(i))