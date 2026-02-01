n = int(input())
arr = sorted(list(map(int, input().split())))
if n & 1:
    cost = 0
    for i in arr:
        cost += abs(i - arr[n >> 1])
    print(cost)
else:
    cost1 = 0
    for i in arr:
        cost1 += abs(i - arr[n >> 1])
    cost2 = 0
    for i in arr:
        cost2 += abs(i - arr[n // 2 - 1])
    print(min(cost1, cost2))