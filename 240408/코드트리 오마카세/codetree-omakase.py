L, Q = map(int, input().split())

order = [list(input().split()) for _ in range(Q)]

s_lst = dict()
p_lst = dict()

t = 0
o_cnt = 0


def action(ordr):
    if ordr[0] == "100":
        # 초밥 제작
        if int(ordr[2]) in s_lst:
            temp = s_lst.get(int(ordr[2]))
        else:
            temp = []
        temp.append(ordr[3])
        s_lst[int(ordr[2])] = temp
    elif ordr[0] == "200":
        # 손님 착석
        p_lst[int(ordr[2])] = [ordr[3], int(ordr[4])]
    elif ordr[0] == "300":
        # 사진 찍기
        p_cnt = len(p_lst)
        s_cnt = 0
        for s in s_lst:
            s_cnt += len(s_lst.get(s))
        print(p_cnt, s_cnt)


def chk_sushi(m):
    p_key = list(p_lst.keys())
    for idx in p_key:
        for move in range(m+1):
            if ((idx-move) % L) in s_lst and p_lst[idx][0] in s_lst[(idx-move) % L]:
                need_cnt = p_lst[idx][1]
                while need_cnt:
                    if p_lst[idx][0] in s_lst[(idx-move) % L]:
                        tmp = s_lst[(idx-move) % L]
                        tmp.remove(p_lst[idx][0])
                        need_cnt -= 1
                        if len(tmp) == 0:
                            s_lst.pop((idx-move) % L)
                            break
                        else:
                            s_lst[(idx-move) % L] = tmp
                    else:
                        break
                if need_cnt == 0:
                    p_lst.pop(idx)
                else:
                    p_lst[idx] = [p_lst[idx][0], need_cnt]
            if len(p_lst) == 0 or len(s_lst) == 0:
                break


# 시간 스킵 하는 부분 초밥 먹는거 체크
cur_t = 1
for o in order:
    spent_t = int(o[1]) - cur_t
    if spent_t >= 2:
        st_tmp = spent_t if spent_t < L else L
        chk_sushi(st_tmp)
    cur_t = int(o[1])
    if spent_t != 0:
        new_dict = dict()
        for i in s_lst:
            key = i
            val = s_lst.get(i)
            new_dict[(key + spent_t) % L] = val
        s_lst = new_dict

    if o[0] != "300":
        action(o)

    if len(p_lst) != 0:
        chk_sushi(0)

    if o[0] == "300":
        action(o)