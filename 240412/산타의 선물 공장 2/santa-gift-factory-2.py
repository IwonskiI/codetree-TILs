import math


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


Q = int(input())

box_dict = dict()
belt_dict = dict()

for _ in range(Q):
    task = list(map(int, input().split()))

    if task[0] == 100:
        belt_t_num, box_t_num = task[1], task[2]
        for bt_num in range(1, belt_t_num+1):
            belt_dict[bt_num] = [None, None, 0]
        t_num = 3
        for bx_num in range(1, box_t_num+1):
            new_node = Node(bx_num)
            if belt_dict[task[t_num]][0] is None:
                belt_dict[task[t_num]] = [new_node, new_node, 1]
            else:
                f_node, l_node, length = belt_dict.get(task[t_num])
                l_node.next = new_node
                new_node.prev = l_node
                belt_dict[task[t_num]] = [f_node, new_node, length + 1]
            box_dict[bx_num] = new_node
            t_num += 1

    elif task[0] == 200:
        src, dst = task[1], task[2]
        if belt_dict[src][2]:
            s_fst, s_lst, s_len = belt_dict.get(src)
            if belt_dict[dst][2]:
                d_fst, d_lst, d_len = belt_dict.get(dst)
                s_lst.next = d_fst
                d_fst.prev = s_lst
                belt_dict[dst] = [s_fst, d_lst, s_len + d_len]
            else:
                belt_dict[dst] = [s_fst, s_lst, s_len]
            belt_dict[src] = [None, None, 0]
        print(belt_dict[dst][2])

    elif task[0] == 300:
        src, dst = task[1], task[2]
        if belt_dict[src][2] and belt_dict[dst][2]:
            s_change, s_lst, s_len = belt_dict.get(src)
            s_next = s_change.next
            d_change, d_lst, d_len = belt_dict.get(dst)
            d_next = d_change.next
            s_change.next = d_next
            d_change.next = s_next
            if s_next:
                s_next.prev = d_change
                belt_dict[src] = [d_change, s_lst, s_len]
            else:
                belt_dict[src] = [d_change, d_change, 1]
            if d_next:
                d_next.prev = s_change
                belt_dict[dst] = [s_change, d_lst, d_len]
            else:
                belt_dict[dst] = [s_change, s_change, 1]
        elif belt_dict[src][2] == 0 and belt_dict[dst][2]:
            d_change, d_lst, d_len = belt_dict[dst]
            d_next = d_change.next
            d_change.next = None
            if d_next:
                d_next.prev = None
                belt_dict[dst] = [d_next, d_lst, d_len - 1]
            else:
                belt_dict[dst] = [None, None, 0]
            belt_dict[src] = [d_change, d_change, 1]
        elif belt_dict[src][2] and belt_dict[dst][2] == 0:
            s_change, s_lst, s_len = belt_dict[src]
            s_next = s_change.next
            s_change.next = None
            if s_next:
                s_next.prev = None
                belt_dict[src] = [s_next, s_lst, s_len - 1]
            else:
                belt_dict[src] = [None, None, 0]
            belt_dict[dst] = [s_change, s_change, 1]
        print(belt_dict[dst][2])

    elif task[0] == 400:
        src, dst = task[1], task[2]
        move_len = math.floor(belt_dict[src][2]/2)
        if move_len:
            s_fst, s_lst, s_len = belt_dict.get(src)
            d_fst, d_lst, d_len = belt_dict.get(dst)
            s_cur = s_fst
            for _ in range(1, move_len):
                s_cur = s_cur.next
            s_nxt = s_cur.next
            if d_len:
                d_fst.prev = s_cur
                s_cur.next = d_fst
                belt_dict[dst] = [s_fst, d_lst, d_len + move_len]
            else:
                s_cur.next = None
                belt_dict[dst] = [s_fst, s_cur, move_len]
            if s_nxt is None or s_cur == s_lst:
                belt_dict[src] = [None, None, 0]
            else:
                belt_dict[src] = [s_nxt, s_lst, s_len - move_len]
        print(belt_dict[dst][2])

    elif task[0] == 500:
        p_num = task[1]
        cur_box = box_dict[p_num]
        front = cur_box.prev.data if cur_box.prev else -1
        end = cur_box.next.data if cur_box.next else -1
        print(front + 2*end)

    elif task[0] == 600:
        b_num = task[1]
        c_fst, c_lst, c_len = belt_dict.get(b_num)
        a = c_fst.data if c_fst else -1
        b = c_lst.data if c_lst else -1
        c = c_len
        print(a + 2*b + 3*c)