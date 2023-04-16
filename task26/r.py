f = open('26.txt')
v, n = map(int, f.readline().split())
*a, = map(int, f)
a.sort()
k = 0
while v - a[k] >= 0:
    v -= a[k]
    k += 1
print(k)
v += a[k - 1]
mx = a[k - 1]
while k < n and v - a[k] >= 0:
    mx = max(a[k], mx)
    k += 1
print(mx)
