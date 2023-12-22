import matplotlib.pyplot as plt
import numpy as np

def isSafe(x, y, board, N):
    return x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1

def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=' ')
        print()

def solveKT():
    N = 8 
    board = [[-1 for _ in range(N)] for _ in range(N)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    pos = 1
    if not solveKTUtil(board, 0, 0, move_x, move_y, pos, N):
        print("Solution does not exist")
    else:
        return board  

def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos, N):
    if pos == N * N:
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if isSafe(new_x, new_y, board, N):
            board[new_x][new_y] = pos
            if solveKTUtil(board, new_x, new_y, move_x, move_y, pos + 1, N):
                return True
            board[new_x][new_y] = -1
    return False

solution_board = solveKT()

def visualize_knight_tour(board):
    N = len(board)
    chessboard = np.array(board)
    pair_array = np.zeros((N * N, 2), dtype=int)

    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0.5, N, 1))
    ax.set_yticks(np.arange(0.5, N, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which="both")
    ax.imshow(chessboard, cmap="plasma")  

    for i in range(N):
        for j in range(N):
            if chessboard[i, j] != -1:
                ax.text(j, i, str(chessboard[i, j]), ha="center", va="center", fontsize=8)
                pair_array[chessboard[i, j] - 1] = (j, i)

    for k in range(len(pair_array) - 1):
        j, i = pair_array[k]
        next_j, next_i = pair_array[k + 1]
        ax.plot([j, next_j], [i, next_i], color='yellow')  

    plt.show()

visualize_knight_tour(solution_board)
