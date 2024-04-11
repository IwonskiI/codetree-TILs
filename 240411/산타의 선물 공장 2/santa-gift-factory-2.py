from collections import defaultdict
import math
# import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# sys.stdin = open("input.txt", "r")
Q = int(input())
belt_dict = defaultdict(list)
box_dict = dict()

for _ in range(Q):
    task = list(map(int, input().split()))
    fun = task[0]

    if fun == 100:
        n, m = task[1], task[2]
        cnt = 1
        for i in range(3, m + 3):
            box = Node(cnt)
            if len(belt_dict[task[i]]):
                box.prev = belt_dict[task[i]][-1]
                belt_dict[task[i]][-1].next = box
            belt_dict[task[i]].append(box)
            box_dict[cnt] = box
            cnt += 1

    elif fun == 200:
        src, dst = task[1], task[2]
        if len(belt_dict[src]):
            if len(belt_dict[dst]):
                belt_dict[dst][0].prev = belt_dict[src][-1]
                belt_dict[src][-1].next = belt_dict[dst][0]
            belt_dict[dst] = belt_dict[src] + belt_dict[dst]
            belt_dict[src] = []
        print(len(belt_dict[dst]))

    elif fun == 300:
        src, dst = task[1], task[2]
        if len(belt_dict[src]) and len(belt_dict[dst]):
            src_box = belt_dict[src][0]
            dst_box = belt_dict[dst][0]
            belt_dict[src][0], belt_dict[dst][0] = dst_box, src_box
            if len(belt_dict[src]) > 1:
                dst_box.next = belt_dict[src][1]
                belt_dict[src][1].prev = dst_box
            else:
                dst_box.next = None
            if len(belt_dict[dst]) > 1:
                src_box.next = belt_dict[dst][1]
                belt_dict[dst][1].prev = src_box
            else:
                src_box.next = None
        elif len(belt_dict[src]) == 0 and len(belt_dict[dst]):
            dst_box = belt_dict[dst][0]
            belt_dict[src].append(dst_box)
            if len(belt_dict[dst]) > 1:
                dst_box.next.prev = None
            dst_box.next = None
            belt_dict[dst] = belt_dict[dst][1:]
        elif len(belt_dict[src]) and len(belt_dict[dst]) == 0:
            src_box = belt_dict[src][0]
            belt_dict[dst].append(src_box)
            if len(belt_dict[src]) > 1:
                src_box.next.prev = None
            src_box.next = None
            belt_dict[src] = belt_dict[src][1:]
        print(len(belt_dict[dst]))

    elif fun == 400:
        src, dst = task[1], task[2]
        move_len = math.floor(len(belt_dict[src])/2)
        if not move_len:
            pass
        else:
            tmp = belt_dict[src][:move_len]
            if len(belt_dict[dst]):
                tmp[-1].next = belt_dict[dst][0]
                belt_dict[dst][0].prev = tmp[-1]
            else:
                tmp[-1].next = None
            belt_dict[dst] = tmp + belt_dict[dst]
            belt_dict[src] = belt_dict[src][move_len:]
            belt_dict[src][0].prev = None
        print(len(belt_dict[dst]))

    elif fun == 500:
        p_num = task[1]
        cur_box = box_dict[p_num]
        prv = cur_box.prev.data if cur_box.prev else -1
        nxt = cur_box.next.data if cur_box.next else -1
        print(prv + 2 * nxt)

    elif fun == 600:
        b_num = task[1]
        b_len = len(belt_dict[b_num])
        if b_len:
            front = belt_dict[b_num][0].data
            end = belt_dict[b_num][-1].data
        else:
            front, end = -1, -1
        print(front + 2*end + 3*b_len)