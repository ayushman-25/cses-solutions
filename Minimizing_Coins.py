n, x = map(int, input().split())
c = list(map(int, input().split()))
dp = [1 << 60 for _ in range(x + 1)]
dp[0] = 0
for i in range(1, x + 1):
    chck = [dp[i - j] + 1 for j in c if i >= j]
    chck = min(chck) if chck else 1 << 60
    dp[i] = min(dp[i], chck)
print(dp[x] if dp[x] != 1 << 60 else -1)