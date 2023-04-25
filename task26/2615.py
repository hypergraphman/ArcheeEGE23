n, *a = map(int, open('26_2615.txt'))

a.sort()
total_sum = 0
for i in range(n):
    total_sum += a[i]
    if a[i + 1] - total_sum > 1:
        print(total_sum + 1, i + 1)
        break