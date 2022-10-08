while n != 126:
    a = bin(n)[2:]
    if a % 2 == 0:
        a = '1' + a + '0'
    if a % 2 == 1:
        a = '11' + a + '11'
    a = int(a, 2)
    print(a)
