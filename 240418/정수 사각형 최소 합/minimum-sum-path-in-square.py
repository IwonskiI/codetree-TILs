N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
n_board = [[0 for _ in range(N)] for _ in range(N)]
n_board[0][N-1] = board[0][N-1]

# init
for t in range(1, N):
    n_board[0][N-1 - t] = n_board[0][N - t] + board[0][N-1 - t]
    n_board[t][N-1] = n_board[t - 1][N-1] + board[t][N-1]


# dp
for c in range(1, N):
    for r in range(N-2, -1, -1):
        minimum = min(n_board[c][r+1], n_board[c-1][r])
        n_board[c][r] = minimum + board[c][r]

print(n_board[N-1][0])