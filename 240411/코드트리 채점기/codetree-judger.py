import heapq
from collections import defaultdict
# import time
# import sys


# '''
#       아래의 구문은 input.txt 를 read only 형식으로 연 후,
#       앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
#       여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
#       아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

#       따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
#       아래 구문을 사용하기 위해서는 import sys가 필요합니다.

#       단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
# '''
# sys.stdin = open("input.txt", "r")

# # w_heap = waiting heapq
# # j_queue = judging queue
# # hist_dict = history dictionary

Q = int(input())
tasks = [list(input().split()) for _ in range(Q)]
w_heap = [[] for _ in range(301)]
w_dict = defaultdict(list)
d_num_dict = dict()
jid_dict = dict()
hist_dict = dict()
jdom_dict = dict()
j_cnt = []
dom_cnt = 1
answer = 1
# start1, start2, start3, start4, start5, start6 = 0, 0, 0, 0, 0, 0
# end1, end2, end3, end4, end5 = 0, 0, 0, 0, 0
# time_lst = [0, 0, 0, 0, 0, 0]


def chk_domain(cur_dom, j_dom):
    if cur_dom in j_dom:
        return False
    return True


def chk_time(d_arg, t_arg, hist_d):
    if d_arg in hist_d:
        st, et, empty = hist_d.get(d_arg)
        if t_arg < st + 3 * (et - st):
            return False
    return True


# start = time.time()
for task in tasks:
    if task[0] == "100":
        j_cnt = [i for i in range(1, int(task[1])+1)]
        heapq.heapify(j_cnt)
        domain, num = task[2].split("/")
        d_num_dict[domain] = dom_cnt
        heapq.heappush(w_heap[dom_cnt], (1, 0, domain, num))
        w_dict[dom_cnt] = [num]

    elif task[0] == "200":
        domain, num = task[3].split("/")
        if domain not in d_num_dict:
            dom_cnt += 1
            d_num_dict[domain] = dom_cnt
        if num in w_dict[d_num_dict[domain]]:
            continue
        else:
            heapq.heappush(w_heap[d_num_dict[domain]], (int(task[2]), int(task[1]), domain, num))
            w_dict[d_num_dict[domain]].append(num)
            answer += 1

    elif task[0] == "300":
        if len(j_cnt) == 0:
            continue

        min_pri = 50001
        min_dom = 0
        min_time = float("inf")
        tmp_task = (0, 0, 0)
        for dn in list(d_num_dict.values()):
            if not len(w_heap[dn]):
                continue
            chk_task = w_heap[dn][0]
            if chk_domain(chk_task[2], jdom_dict) and chk_time(chk_task[2], int(task[1]), hist_dict):
                if (chk_task[0] < min_pri) or (chk_task[0] == min_pri and min_time > chk_task[1]):
                    min_pri = chk_task[0]
                    min_dom = dn
                    min_time = chk_task[1]
            else:
                continue

        if min_dom:
            chk_task = heapq.heappop(w_heap[min_dom])
            w_dict[d_num_dict[chk_task[2]]].remove(chk_task[3])
            if not len(w_dict[d_num_dict[chk_task[2]]]):
                w_dict.pop(d_num_dict[chk_task[2]])
            cur_j_cnt = heapq.heappop(j_cnt)
            jid_dict[cur_j_cnt] = (int(task[1]), chk_task[2])
            jdom_dict[chk_task[2]] = True
            answer -= 1

    elif task[0] == "400":
        end_t = int(task[1])
        end_id = int(task[2])
        if end_id in jid_dict:
            heapq.heappush(j_cnt, end_id)
            start_t, dom = jid_dict.get(end_id)
            jid_dict.pop(end_id)
            jdom_dict.pop(dom)
            hist_dict[dom] = (start_t, end_t, end_id)
        else:
            continue

    elif task[0] == "500":
        print(answer)

# end = time.time()
# print(f"{end - start:.5f} sec")
# for ti in time_lst:
#     print(f"{ti:.8f} sec")