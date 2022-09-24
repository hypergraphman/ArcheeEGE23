def alg(n):
    s1 = f'{n:b}'
    s2a = s1 + str(sum(map(int, s1)) % 2)
    s2b = s2a + str(s2a.count('1') % 2)
    r = int(s2b, 2)
    return r


i = 1
while alg(i) <= 77:
    i += 1
print(i)

for i in range(28):
    if alg(i) > 77:
        print(i)
        break
