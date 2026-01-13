def rec(n, f, t, x):
    if n == 0:
        return
    rec(n - 1, f, x, t)
    print(f, t)
    rec(n - 1, x, t, f)

n = int(input())
print(2 ** n - 1)
rec(n, 1, 3, 2)