import heapq

# w_heap = waiting heapq
# j_queue = judging queue
# hist_dict = history dictionary

Q = int(input())
tasks = [list(input().split()) for _ in range(Q)]
w_heap = []
w_dict = dict()
jid_dict = dict()
hist_dict = dict()
jdom_dict = dict()
j_cnt = []


def chk_domain(cur_dom, j_dom):
    domain = cur_dom.split("/")[0]
    if domain in j_dom:
        return False
    return True


def chk_time(d_arg, t_arg, hist_d):
    domain = d_arg.split("/")[0]
    if domain in hist_d:
        st = hist_d.get(domain)[0]
        gap = hist_d.get(domain)[1] - st
        if t_arg < st + 3 * gap:
            return False
    return True


for task in tasks:
    if task[0] == "100":
        j_cnt = [i for i in range(1, int(task[1])+1)]
        heapq.heapify(j_cnt)
        heapq.heappush(w_heap, (1, 0, task[2]))
        w_dict[task[2]] = True

    elif task[0] == "200":
        if task[3] not in w_dict:
            heapq.heappush(w_heap, (int(task[2]), int(task[1]), task[3]))
            w_dict[task[3]] = True
        else:
            continue

    elif task[0] == "300":
        if len(j_cnt) == 0:
            continue
        # chk domain
        # chk valid time(hist)
        task_lst = []
        while w_heap:
            chk_task = heapq.heappop(w_heap)
            if chk_domain(chk_task[2], jdom_dict) and chk_time(chk_task[2], int(task[1]), hist_dict):
                w_dict.pop(chk_task[2])
                cur_j_cnt = heapq.heappop(j_cnt)
                jid_dict[cur_j_cnt] = (int(task[1]), chk_task[2].split("/")[0])
                jdom_dict[chk_task[2].split("/")[0]] = True
                break
            else:
                task_lst.append(chk_task)
        w_heap = task_lst + w_heap
        heapq.heapify(w_heap)

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
        print(len(w_heap))