from collections import defaultdict
import math
import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# sys.stdin = open("input.txt", "r")
Q = int(input())
st_ed_dict = defaultdict(list)
box_dict = dict()

for _ in range(Q):
    task = list(map(int, input().split()))
    fun = task[0]

    if fun == 100:
        n, m = task[1], task[2]
        belt_dict = defaultdict(list)
        cnt = 1
        for i in range(3, m + 3):
            box = Node(cnt)
            if len(belt_dict[task[i]]):
                box.prev = belt_dict[task[i]][-1]
                belt_dict[task[i]][-1].next = box
            belt_dict[task[i]].append(box)
            box_dict[cnt] = box
            cnt += 1
        for bd in list(belt_dict.keys()):
            st_ed_dict[bd] = [belt_dict[bd][0], belt_dict[bd][-1], len(belt_dict[bd])]

    elif fun == 200:
        src, dst = task[1], task[2]
        if src not in st_ed_dict:
            st_ed_dict[src] = [None, None, 0]
        if dst not in st_ed_dict:
            st_ed_dict[dst] = [None, None, 0]
        if not (st_ed_dict[src][0] is None and st_ed_dict[src][1] is None):
            src_lst = st_ed_dict[src]
            if not (st_ed_dict[dst][0] is None and st_ed_dict[dst][1] is None):
                dst_lst = st_ed_dict[dst]
                dst_lst[0].prev = src_lst[1]
                src_lst[1].next = dst_lst[0]
                st_ed_dict[dst] = [st_ed_dict[src][0], st_ed_dict[dst][1], src_lst[2] + dst_lst[2]]
                st_ed_dict[src] = [None, None, 0]
            else:
                st_ed_dict[dst] = [st_ed_dict[src][0], st_ed_dict[src][1], src_lst[2]]
                st_ed_dict[src] = [None, None, 0]
        print(st_ed_dict[dst][2])

    elif fun == 300:
        src, dst = task[1], task[2]
        src_lst = st_ed_dict[src] if src in st_ed_dict else [None, None, 0]
        dst_lst = st_ed_dict[dst] if dst in st_ed_dict else [None, None, 0]
        if src_lst[2] and dst_lst[2]:
            s_next = src_lst[0].next
            d_next = dst_lst[0].next
            src_lst[0].next = d_next
            dst_lst[0].next = s_next
            if s_next:
                s_next.prev = dst_lst[0]
            if d_next:
                d_next.prev = src_lst[0]
            d_tmp = dst_lst[0]
            s_tmp = src_lst[0]
            st_ed_dict[src][0] = d_tmp
            if st_ed_dict[src][2] == 1:
                st_ed_dict[src][1] = d_tmp
            st_ed_dict[dst][0] = s_tmp
            if st_ed_dict[dst][2] == 1:
                st_ed_dict[dst][1] = s_tmp
        elif src_lst[2] == 0 and dst_lst[2]:
            d_next = dst_lst[0].next
            dst_lst[0].next = None
            if d_next:
                d_next.prev = None
                st_ed_dict[dst] = [d_next, dst_lst[1], dst_lst[2] - 1]
            else:
                st_ed_dict[dst] = [None, None, 0]
            st_ed_dict[src] = [dst_lst[0], dst_lst[0], 1]
        elif dst_lst[2] == 0 and src_lst[2]:
            s_next = src_lst[0].next
            src_lst[0].next = None
            if s_next:
                s_next.prev = None
                st_ed_dict[src] = [s_next, src_lst[1], src_lst[2] - 1]
            else:
                st_ed_dict[src] = [None, None, 0]
            st_ed_dict[dst] = [src_lst[0], src_lst[0], 1]
        if dst in st_ed_dict:
            print(st_ed_dict[dst][2])
        else:
            print(0)

    elif fun == 400:
        src, dst = task[1], task[2]
        if src not in st_ed_dict:
            st_ed_dict[src] = [None, None, 0]
        if dst not in st_ed_dict:
            st_ed_dict[dst] = [None, None, 0]
        move_len = math.floor(st_ed_dict[src][2]/2)
        if not move_len:
            pass
        else:
            start_box = st_ed_dict[src][0]
            for _ in range(1, move_len):
                start_box = start_box.next
            next_box = start_box.next
            if st_ed_dict[dst][2]:
                start_box.next = st_ed_dict[dst][0]
                st_ed_dict[dst][0].prev = start_box
            else:
                start_box.next = None
            st_ed_dict[src][2] -= move_len
            st_ed_dict[dst][2] += move_len

            st_ed_dict[src][0] = next_box
            next_box.prev = None
            st_ed_dict[dst][0] = start_box
            if not st_ed_dict[dst][1]:
                st_ed_dict[dst][1] = start_box
        print(st_ed_dict[dst][2])

    elif fun == 500:
        p_num = task[1]
        cur_box = box_dict[p_num]
        prv = cur_box.prev.data if cur_box.prev else -1
        nxt = cur_box.next.data if cur_box.next else -1
        print(prv + 2 * nxt)

    elif fun == 600:
        b_num = task[1]
        if b_num in st_ed_dict:
            b_len = st_ed_dict[b_num][2]
        else:
            b_len = 0
        if b_len:
            front = st_ed_dict[b_num][0].data
            end = st_ed_dict[b_num][1].data
        else:
            front, end = -1, -1
        print(front + 2*end + 3*b_len)