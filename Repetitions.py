s = input()
cmpr = s[0]
bffr = 1
ans = 0
for i in range(1, len(s)):
    if s[i] == cmpr:
        bffr += 1
    else:
        ans = max(ans, bffr)
        bffr = 1
        cmpr = s[i]
print(max(ans, bffr))