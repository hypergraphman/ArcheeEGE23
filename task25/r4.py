import time

start = time.time()
for i in range(2023, 2*10**9 + 1, 2023):
    s = str(i)
    if s[0] == '1' and s[2:5 + 1] == '2139' and s[-1] == '4':
        print(i, i // 2023)
print(time.time() - start)

from fnmatch import fnmatch

start = time.time()
for i in range(2023, 2*10**9 + 1, 2023):
    if fnmatch(str(i), '1?2139*4'):
        print(i, i // 2023)
print(time.time() - start)


from re import fullmatch

start = time.time()
for i in range(2023, 2*10**9 + 1, 2023):
    if fullmatch(r'1\d2139\d*4', str(i)):
        print(i, i // 2023)
print(time.time() - start)