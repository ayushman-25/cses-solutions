n = int(input())
ans = 0
itr = 1
while itr <= n:
    itr *= 5
    ans += n // itr
print(ans)