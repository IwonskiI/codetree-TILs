class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


Q = int(input())
belt_lst = []
id_dict = dict()
for _ in range(Q):
    task = list(map(int, input().split()))

    if task[0] == 100:
        # 공장 설립
        n, m = task[1], task[2]
        b_cnt = n//m
        id_lst = task[3: n+3]
        w_lst = task[n+3:]
        belt_num = 0
        belt_node = Node(belt_num)
        new_node = None
        s_node, e_node = None, None
        for idx in range(n):
            prev_node = new_node
            new_node = Node((id_lst[idx], w_lst[idx]))
            new_node.prev = prev_node
            if not prev_node:
                s_node = new_node
            else:
                prev_node.next = new_node
            if idx % b_cnt == 0 and idx != 0:
                prev_node.next = None
                belt_lst.append((s_node, prev_node))
                s_node = new_node
                new_node.prev = None
                belt_num += 1
                belt_node = Node(belt_num)
            id_dict[id_lst[idx]] = (belt_node, new_node)
        new_node.next = None
        belt_lst.append((s_node, new_node))

    elif task[0] == 200:
        w_max = task[1]
        w_tot = 0
        for b_len in range(len(belt_lst)):
            if belt_lst[b_len] == -1:
                continue
            cur_box, last_box = belt_lst[b_len]
            if cur_box.data[1] <= w_max:
                w_tot += cur_box.data[1]
                next_box = cur_box.next
                next_box.prev = None
                belt_lst[b_len] = (next_box, last_box)
                id_dict.pop(cur_box.data[0])
            else:
                next_box = cur_box.next
                next_box.prev = None
                last_box.next = cur_box
                cur_box.prev = last_box
                cur_box.next = None
                belt_lst[b_len] = (next_box, cur_box)
        print(w_tot)

    elif task[0] == 300:
        r_id = task[1]
        if r_id in id_dict:
            empty, r_box = id_dict.get(r_id)
            p_r_box = r_box.prev
            n_r_box = r_box.next
            if p_r_box:
                p_r_box.next = n_r_box
            if n_r_box:
                n_r_box.prev = p_r_box
            id_dict.pop(r_id)
            print(r_id)
        else:
            print(-1)

    elif task[0] == 400:
        f_id = task[1]
        if f_id in id_dict:
            belt_num, f_box = id_dict.get(f_id)
            belt_num = belt_num.data
            front_box, last_box = belt_lst[belt_num]
            if front_box == f_box:
                pass
            elif last_box == f_box:
                prev_box = f_box.prev
                prev_box.next = None
                front_box.prev = f_box
                f_box.next = front_box
                f_box.prev = None
                belt_lst[belt_num] = (f_box, prev_box)
            else:
                p_f_box = f_box.prev
                p_f_box.next = None
                f_box.prev = None
                last_box.next = front_box
                front_box.prev = last_box
                belt_lst[belt_num] = (f_box, p_f_box)
            print(belt_num+1)
        else:
            print(-1)

    elif task[0] == 500:
        b_num = task[1] - 1
        if belt_lst[b_num] == -1:
            print(-1)
            continue
        move_num = -1
        belt_len = len(belt_lst)
        for belt in range(1, belt_len):
            if belt_lst[(belt+b_num) % belt_len] == -1:
                continue
            else:
                move_num = ((belt+b_num) % belt_len)
                break
        last_box = belt_lst[move_num][1]
        first_box = belt_lst[b_num][0]
        id_dict.get(first_box.data[0])[0].data = move_num
        first_box.prev = last_box
        last_box.next = first_box
        print(task[1])
        belt_lst[b_num] = -1