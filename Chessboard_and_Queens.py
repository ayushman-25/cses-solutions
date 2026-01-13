d1 = [False for _ in range(16)]
d2 = [False for _ in range(16)]
col = [False for _ in range(8)]
board = [input() for _ in range(8)]
ans = 0

def rec(r) -> None:
    global ans
    if r == 8:
        ans += 1
        return
    for c in range(8):
        if board[r][c] == '*':
            continue
        if col[c] or d1[r + c] or d2[r - c + 7]:
            continue
        col[c] = d1[r + c] = d2[r - c + 7] = True
        rec(r + 1)
        col[c] = d1[r + c] = d2[r - c + 7] = False

rec(0)
print(ans)