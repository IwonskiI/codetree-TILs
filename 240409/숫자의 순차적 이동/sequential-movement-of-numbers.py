n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

pos_dict = dict()

for i in range(n):
    for j in range(n):
        pos_dict[board[i][j]] = [i, j]


def search(num):
    global n, m, board, pos_dict

    c, r = pos_dict[num]
    max_num = 0
    dc = [1, -1, 0, 0, 1, 1, -1, -1]
    dr = [0, 0, -1, 1, -1, 1, -1, 1]
    mc, mr = 0, 0

    for i in range(8):
        nc, nr = c + dc[i], r + dr[i]
        if nc < 0 or nr < 0 or nc >= n or nr >= n:
            continue
        if board[nc][nr] > max_num:
            max_num = board[nc][nr]
            mc, mr = nc, nr
    board[c][r], board[mc][mr] = board[mc][mr], board[c][r]
    pos_dict[num] = [mc, mr]
    pos_dict[max_num] = [c, r]


for t in range(m):
    for numb in range(1, n * n + 1):
        search(numb)

for bc in board:
    for br in bc:
        print(br, end = " ")
    print()