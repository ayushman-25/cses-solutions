n = int(input())
for i in range(0, 1 << n):
    gc = (bin(i ^ (i >> 1))[2:])
    gc = '0' * (n - len(gc)) + gc
    print(gc)

# n = int(input())
# gc = ["0", "1"]
# for i in range(n - 1):
#     hmm = gc[:]
#     curr_gc = list()
#     for i in hmm:
#         curr_gc.append('0' + i)
#     hmm.reverse()
#     for i in hmm:
#         curr_gc.append('1' + i)
#     gc = curr_gc
# for i in gc:
#     print(i)