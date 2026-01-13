t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x >= y:
        print(x * x - x + 1 + (-(x - y) if x & 1 else (x - y)))
    else:
        print(y * y - y + 1 + ((y - x) if y & 1 else -(y - x)))