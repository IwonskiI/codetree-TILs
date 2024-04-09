def init(lst):
    if lst[0] != 2:
        return int(lst[1])-1
    else:
        if lst[1] == 'L':
            return 0
        elif lst[1] == 'U':
            return 1
        elif lst[1] == 'R':
            return 2
        elif lst[1] == 'D':
            return 3


def move(info, b, n):
    c, r, d = info
    # d = [L U R D]
    dc = [0, -1, 0, 1]
    dr = [-1, 0, 1, 0]
    nc, nr = c + dc[d], r + dr[d]
    if nc >= n or nr >= n or nc < 0 or nr < 0:
        info[2] = (d + 2) % 4
    else:
        b[c][r] -= 1
        b[nc][nr] += 1
        info[0] = nc
        info[1] = nr


def remove_ball(b, info):
    for bc in range(len(b)):
        for br in range(len(b)):
            if b[bc][br] > 1:
                b[bc][br] = 0
                for ind, b_if in enumerate(info):
                    if [bc, br] == [b_if[0], b_if[1]]:
                        del info[ind]


T = int(input())

for t in range(T):

    N, M = map(int, input().split())
    b_info = [list(map(init, enumerate(input().split()))) for _ in range(M)]
    board = [[0 for _ in range(N)] for _ in range(N)]

    for ball in b_info:
        board[ball[0]][ball[1]] = 1

    for _ in range(2 * N - 1):
        for ball in b_info:
            move(ball, board, N)
        remove_ball(board, b_info)

    print(sum([sum(board[r]) for r in range(N)]))