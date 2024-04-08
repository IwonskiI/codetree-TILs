L, Q = map(int, input().split())

order = [list(input().split()) for _ in range(Q)]

s_lst = dict()
p_lst = dict()

t = 0
o_cnt = 0


def action(ord):
    if ord[0] == "100":
        # 초밥 제작
        if int(ord[2]) in s_lst:
            temp = s_lst.get(int(ord[2]))
        else:
            temp = []
        temp.append(ord[3])
        s_lst[int(ord[2])] = temp
    elif ord[0] == "200":
        # 손님 착석
        p_lst[int(ord[2])] = [ord[3], int(ord[4])]
    elif ord[0] == "300":
        # 사진 찍기
        p_cnt = len(p_lst)
        s_cnt = 0
        for s in s_lst:
            s_cnt += len(s_lst.get(s))
        print(p_cnt, s_cnt)


def chk_sushi():
    p_key = list(p_lst.keys())
    for idx in p_key:
        while True:
            if idx in s_lst:
                if p_lst[idx][0] in s_lst[idx]:
                    tmp = s_lst[idx]
                    tmp.remove(p_lst[idx][0])
                    s_lst[idx] = tmp
                    p_lst[idx] = [p_lst[idx][0], p_lst[idx][1] - 1]
                    if p_lst[idx][1] == 0:
                        p_lst.pop(idx)
                        break
                else:
                    break
            else:
                break


cur_t = 1
for o in order:
    spent_t = int(o[1]) - cur_t
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
        chk_sushi()

    if o[0] == "300":
        action(o)