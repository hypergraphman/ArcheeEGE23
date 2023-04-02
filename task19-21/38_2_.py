win = 51


def f(a, c, m):
    if a >= win:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = []
    if (a + 1) % 2 == 1:
        moves.append(f(a + 1, c + 1, m))
    if (a + 3) % 2 == 1:
        moves.append(f(a + 3, c + 1, m))
    if (a * 3) % 2 == 1:
        moves.append(f(a * 3, c + 1, m))
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, win):
    for m in range (1, 4 + 1):
        if f(s, 0, m):
            print(s, m)
            break
