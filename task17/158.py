f = open('17-1.txt')
*a, = map(int, f.read().split())
f.close()
cur_len = 1
max_len = 1
amount = 1
for p1, p2 in zip(a, a[1:]):
    if p1 > p2:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
            amount = 1
        elif cur_len == max_len:
            amount += 1
    else:
        cur_len = 1
print(max_len, amount)