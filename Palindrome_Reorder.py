from collections import Counter

s = input()
cnt = Counter(s)
odd_cnt = sum([cnt[i] & 1 for i in cnt.keys()])
if odd_cnt >= 2:
    print("NO SOLUTION")
    exit(0)
ans = ['' for _ in range(len(s))]
l, r = 0, len(ans) - 1
for i in cnt.keys():
    if cnt[i] & 1:
        continue
    while cnt[i]:
        ans[l] = i
        ans[r] = i
        cnt[i] -= 2
        l += 1
        r -= 1
if odd_cnt:
    for i in cnt.keys():
        if cnt[i] & 1:
            while cnt[i]:
                ans[l] = i
                cnt[i] -= 1
                l += 1
print("".join(ans))