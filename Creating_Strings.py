from itertools import permutations
s = input()
ls = list(set(permutations(s)))
ls.sort()
print(len(ls))
for i in ls:
    print("".join(i))