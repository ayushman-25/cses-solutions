n = int(input())
for k in range(1, n + 1):
    print((k ** 4 - 9 * k ** 2 + 24 * k - 16) >> 1)