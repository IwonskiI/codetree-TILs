from collections import deque


def dfs(start, c, p):
    depth = 0
    stack = deque([[start, depth]])
    answer = 0

    while stack:
        n, d = stack.pop()
        if n not in c:
            continue
        for child in c[n]:
            stack.append([child, d + 1])
            if p[child][1] > d:
                answer += 1

    return answer


N, Q = map(int, input().split())
order = [list(map(int, input().split())) for _ in range(Q)]

p_graph = dict()
c_graph = dict()

for i in range(1, N+1):
    if order[0][i] in c_graph:
        c_graph[order[0][i]] = c_graph.get(order[0][i]) + [i]
    else:
        c_graph[order[0][i]] = [i]
    p_graph[i] = [order[0][i], order[0][i + N]]

for o in order:
    node_num = o[1]
    if o[0] == 100:
        # 초기 세팅
        continue
    elif o[0] == 200:
        # 알림망
        parent = p_graph[node_num][0]
        if node_num in c_graph.get(parent):
            c_graph.get(parent).remove(node_num)
        else:
            tmp = c_graph.get(parent)
            tmp.append(node_num)
            c_graph[parent] = tmp

    elif o[0] == 300:
        # 권한 변경
        d_power = o[2]
        p_graph[node_num] = [p_graph.get(node_num)[0], d_power]
    elif o[0] == 400:
        # 부모 교환
        node_num2 = o[2]
        p_num1 = p_graph.get(node_num)
        p_num2 = p_graph.get(node_num2)
        p_graph[node_num] = [p_num2[0], p_num1[1]]
        p_graph[node_num2] = [p_num1[0], p_num2[1]]
        if node_num in c_graph[p_num1[0]]:
            c_graph.get(p_num1[0]).remove(node_num)
            c_graph.get(p_num2[0]).append(node_num)
        if node_num2 in c_graph[p_num2[0]]:
            c_graph.get(p_num2[0]).remove(node_num2)
            c_graph.get(p_num1[0]).append(node_num2)
    elif o[0] == 500:
        # 채팅방 수 조회
        print(dfs(node_num, c_graph, p_graph))