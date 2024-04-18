N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
n_board = [[0 for _ in range(N)] for _ in range(N)]
n_board[0][0] = board[0][0]

# init
for t in range(1, N):
    n_board[0][t] = min(n_board[0][t - 1], board[0][t])
    n_board[t][0] = min(n_board[t - 1][0], board[t][0])

# dp
for c in range(1, N):
    for r in range(1, N):
        maximum = max(n_board[c][r - 1], n_board[c - 1][r])
        n_board[c][r] = min(maximum, board[c][r])

print(n_board[N-1][N-1])