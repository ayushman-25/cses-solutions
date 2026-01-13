n = int(input())
arr = list(map(int, input().split()))
sm = sum(arr)
ans = 1 << 60
for b in range(2 ** n):
    s1 = 0
    for i in range(n):
        if b & (1 << i):
            s1 += arr[i]
    ans = min(ans, abs(sm - s1 * 2))
print(ans)
