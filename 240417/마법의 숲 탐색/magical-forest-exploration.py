def chk_u(col, row):
    global board

    if row == -1:
        if board[col - 1][row + 1] == 0:
            return True
        else:
            return False
    elif row == 0:
        if board[col - 1][row + 1] == 0 and board[col - 1][row] == 0 and board[col - 2][row] == 0:
            return True
        else:
            return False
    else:
        if board[col - 1][row + 1] == 0 and board[col - 1][row] == 0 and board[col - 2][row] == 0 and board[col - 2][row - 1] == 0:
            return True
        else:
            return False


def chk_d(col, row):
    global board

    if row == -1:
        if board[col + 1][row + 1] == 0:
            return True
        else:
            return False
    elif row == 0:
        if board[col + 1][row + 1] == 0 and board[col + 1][row] == 0 and board[col + 2][row] == 0:
            return True
        else:
            return False
    else:
        if board[col + 1][row + 1] == 0 and board[col + 1][row] == 0 and board[col + 2][row] == 0 and board[col + 2][row - 1] == 0:
            return True
        else:
            return False


def chk_space(col, row=-1):
    global board, R, C, recur

    while row < R - 1:
        if row == -1:
            if board[col][row+1] != 0:
                break
        if row >= 0:
            if board[col][row+1] != 0 or board[col+1][row] != 0 or board[col-1][row] != 0:
                break
        row += 1

    if row != R - 1:
        if 1 <= col-1 and chk_u(col, row):
            recur -= 1
            col, row = chk_space(col - 1, row)
        elif col+1 <= C-2 and chk_d(col, row):
            recur += 1
            col, row = chk_space(col + 1, row)

    if row < 2:
        return [-1, -1]

    return [col, row]


def arrived(col, row, ex_dir, gn):
    global board, R, C, g_dict
    dc = [0, 1, 0, -1]
    dr = [-1, 0, 1, 0]

    board[col][row] = gn
    for dd in range(4):
        nc, nr = col + dc[dd], row + dr[dd]
        if dd == ex_dir:
            board[nc][nr] = -gn
            g_dict[gn].append([nc, nr])
        else:
            board[nc][nr] = gn


def calc_score(gn, v=None):
    global board, g_dict, s_dict, R
    dc = [0, 1, 0, -1]
    dr = [-1, 0, 1, 0]

    if gn in s_dict:
        return s_dict.get(gn)

    if v is None:
        v = dict()
    ctr, ex = g_dict.get(gn)
    ctr_c, ctr_r = ctr
    ex_c, ex_r = ex
    point = ctr_r + 1

    if point == R - 1:
        s_dict[gn] = R - 1
        return R - 1

    for dd in range(4):
        nex_c, nex_r = ex_c + dc[dd], ex_r + dr[dd]
        in_range = 0 <= nex_c < C and 0 <= nex_r < R
        if not in_range:
            continue
        if board[nex_c][nex_r] == gn:
            continue
        else:
            if board[nex_c][nex_r] > 0:
                if board[nex_c][nex_r] in v:
                    continue
                v[board[nex_c][nex_r]] = True
                temp = calc_score(board[nex_c][nex_r], v)
                point = max(point, temp)
                if point == R - 1:
                    s_dict[gn] = R - 1
                    return R - 1
            elif board[nex_c][nex_r] < 0:
                if -board[nex_c][nex_r] in v:
                    continue
                v[-board[nex_c][nex_r]] = True
                temp = calc_score(-board[nex_c][nex_r], v)
                point = max(point, temp)
                if point == R - 1:
                    s_dict[gn] = R - 1
                    return R - 1

    return point


R, C, K = map(int, input().split())

board = [[0 for _ in range(R)] for _ in range(C)]
g_dict = dict()
s_dict = dict()
total_score = 0

for g_num in range(1, K+1):
    # 위: 0 / 왼: 1 / 아: 2 / 오: 3
    g_row, e_pos = map(int, input().split())
    recur = 0
    e_col, e_row = chk_space(g_row - 1)

    if e_col == -1 and e_row == -1:
        board = [[0 for _ in range(R)] for _ in range(C)]
        g_dict = dict()
    else:
        g_dict[g_num] = [[e_col, e_row - 1]]
        arrived(e_col, e_row - 1, (e_pos + (recur % 4)) % 4, g_num)
        total_score += (calc_score(g_num)+1)

print(total_score)