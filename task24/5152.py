a = open('24-203.txt').readline().strip()
k = 0
for i in range(2, 40):
    for j in range(len(a) - i):
        b = []
        for x in range(j, i + j + 1):
            b.append(a[x])
        if b.count('A') == 0 or b.count('B') == 0 or b.count('C') == 0:
            k += 1
            # print(b)
print(k)