def chk_tree(col, row):
    global N, board, s_left
    ddc = [-1, 0, 0, 1]
    ddr = [0, -1, 1, 0]
    near_tree = 0
    space = 0
    for ddd in range(4):
        nnc, nnr = col + ddc[ddd], row + ddr[ddd]
        if 0 > nnc or 0 > nnr or nnc >= N or nnr >= N:
            continue
        if board[nnc][nnr] == 0 and s_left[nnc][nnr] == 0:
            space += 1
        if board[nnc][nnr] > 0:
            near_tree += 1
    return [space, near_tree]


def chk_spray(col, row):
    global N, K, board
    dig_c = [-1, -1, 1, 1]
    dig_r = [-1, 1, -1, 1]
    t_cnt = board[col][row]
    for dig_d in range(4):
        ran = K
        dnc, dnr = col + dig_c[dig_d], row + dig_r[dig_d]
        while ran:
            if 0 > dnc or 0 > dnr or dnc >= N or dnr >= N:
                break
            if board[dnc][dnr] <= 0:
                break
            t_cnt += board[dnc][dnr]
            dnc, dnr = dnc + dig_c[dig_d], dnr + dig_r[dig_d]
            ran -= 1
    return t_cnt


def spray_tree(col, row):
    global N, K, C, board
    dig_c = [-1, -1, 1, 1]
    dig_r = [-1, 1, -1, 1]

    board[col][row] = 0
    s_left[col][row] = C + 1

    for dig_d in range(4):
        ran = K
        dnc, dnr = col + dig_c[dig_d], row + dig_r[dig_d]
        while ran:
            if 0 > dnc or 0 > dnr or dnc >= N or dnr >= N:
                break
            s_left[dnc][dnr] = C + 1
            if board[dnc][dnr] <= 0:
                break
            board[dnc][dnr] = 0
            dnc, dnr = dnc + dig_c[dig_d], dnr + dig_r[dig_d]
            ran -= 1


N, M, K, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
total_cut = 0

# 제초제 남은 년수
s_left = [[0 for _ in range(N)] for _ in range(N)]
dc = [-1, 0, 0, 1]
dr = [0, -1, 1, 0]

# m years spent
for _ in range(M):
    # 최대 박멸 수, col 좌표, row 좌표
    max_cut = [0, 99, 99]
    left_tree = False

    for c in range(N):
        for r in range(N):
            if s_left[c][r] > 0:
                s_left[c][r] -= 1
            if board[c][r] > 0:
                left_tree = True

    if not left_tree:
        break

    add_lst = [bi[:] for bi in board]

    for c in range(N):
        for r in range(N):
            if board[c][r] > 0:
                n_tree = chk_tree(c, r)
                add_lst[c][r] += n_tree[1]
                if n_tree[0] > 0:
                    add_cnt = add_lst[c][r] // n_tree[0]
                    for dd in range(4):
                        nc, nr = c + dc[dd], r + dr[dd]
                        if 0 > nc or 0 > nr or nc >= N or nr >= N or board[nc][nr] != 0 or s_left[nc][nr] != 0:
                            continue
                        add_lst[nc][nr] += add_cnt

    board = add_lst

    for c in range(N):
        for r in range(N):
            if board[c][r] > 0:
                cut_cnt = chk_spray(c, r)
                if cut_cnt > max_cut[0]:
                    max_cut = [cut_cnt, c, r]

    spray_tree(max_cut[1], max_cut[2])
    total_cut += max_cut[0]

print(total_cut)