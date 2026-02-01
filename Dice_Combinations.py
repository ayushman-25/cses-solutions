n = int(input())
mod = int(1e9) + 7
dp = [0 for _ in range(n + 1)]
dp[0] = 1
for i in range(1, n + 1):
    for d in range(1, 7):
        if i - d >= 0:
            dp[i] = (dp[i - d] + dp[i]) % mod
print(dp[n])