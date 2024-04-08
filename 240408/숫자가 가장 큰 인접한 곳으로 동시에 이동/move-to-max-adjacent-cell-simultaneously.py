def move(x, y, d, nv):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    nv[x+dx[d]][y+dy[d]] += 1

def chk_dir(g, x, y, n, v):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    d = 0
    max_cnt = 0

    for i in range(4):
        nx , ny = x + dx[i], y + dy[i]
        if nx >= n or ny >= n or nx < 0 or ny < 0:
            continue
        if g[nx][ny] > max_cnt:
            d = i
            max_cnt = g[nx][ny]
    
    move(x, y, d, v)
        


n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
b_board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    b_board[x-1][y-1] = 1

for time in range(t):
    n_board = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if b_board[r][c] == 1:
                chk_dir(board, r, c, n, n_board)
    b_board = [n_b[:] for n_b in n_board]

    for cb in b_board:
        for rb in cb:
            if rb > 1:
                rb = 0

print(sum([sum(br) for br in b_board]))