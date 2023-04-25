print('1 2 3 f\'')
for x1 in 0, 1:
    for x2 in 0, 1:
        for x3 in 0, 1:
            x1 = int(not x1)
            x2 = int(not x2)
            x3 = int(not x3)
            f = x1 and x2 or x2 and x3 or x3 and x1
            print(x1, x2, x3, int(f))
