n = int(input())
sm = n * (n + 1) >> 1
if sm & 1:
    print("NO")
    exit(0)
sm >>= 1
l1 = list()
used = [0 for _ in range(n)]
l1.append(n)
itr = n
s = n
used[n - 1] = 1
while s < sm:
    if sm - s - 1 < n and not used[sm - s - 1]:
        l1.append(sm - s)
        used[sm - s - 1] = 1
        break
    else:
        l1.append(itr - 1)
        used[itr - 2] = 1
        itr -= 1
        s += itr
if sum(l1) != sm:
    print("NO")
    exit(0)
print("YES")
print(len(l1))
print(*l1)
print(n - len(l1))
print(*[i + 1 for i in range(n) if not used[i]])