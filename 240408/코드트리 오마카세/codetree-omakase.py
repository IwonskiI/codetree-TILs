L, Q = map(int, input().split())

order = [list(input().split()) for _ in range(Q)]

s_lst = [[] for _ in range(L)]
p_lst = [[] for _ in range(L)]
seat_lst = []

t = 0
o_cnt = 0


def action(o):
    if o[0] == "100":
        # 초밥 제작
        s_lst[int(o[2])].append(o[3])
    elif o[0] == "200":
        # 손님 착석
        p_lst[int(o[2])] = [o[3], int(o[4])]
        seat_lst.append(int(o[2]))
    elif o[0] == "300":
        # 사진 찍기
        p_cnt = len(seat_lst)
        s_cnt = 0
        for s in s_lst:
            s_cnt += len(s)
        print(p_cnt, s_cnt)


def chk_sushi():
    for idx in seat_lst:
        while True:
            if p_lst[idx][0] in s_lst[idx]:
                s_lst[idx].remove(p_lst[idx][0])
                p_lst[idx][1] -= 1
                if p_lst[idx][1] == 0:
                    p_lst[idx] = []
                    seat_lst.remove(idx)
                    break
            else:
                break


while True:
    t += 1
    if int(order[o_cnt][1]) == t and order[o_cnt][0] != "300":
        action(order[o_cnt])
        o_cnt += 1

    if len(seat_lst) != 0:
        chk_sushi()
    s_lst = [s_lst[-1]] + s_lst[:-1]

    if int(order[o_cnt][1]) == t and order[o_cnt][0] == "300":
        action(order[o_cnt])
        o_cnt += 1

    if o_cnt == Q:
        break