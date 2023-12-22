import matplotlib.pyplot as plt
import numpy as np

BOARD_SIZE = 8
MOVES = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

def is_within_board(x, y):
    return (0 <= x < BOARD_SIZE) and (0 <= y < BOARD_SIZE)

def generate_closed_tour():
    board = np.full((BOARD_SIZE, BOARD_SIZE), -1)
    x, y = 4, 0
    board[y][x] = 1

    for step in range(2, BOARD_SIZE ** 2 + 1):
        possible_moves = []
        for dx, dy in MOVES:
            new_x, new_y = x + dx, y + dy
            if is_within_board(new_x, new_y) and board[new_y][new_x] == -1:
                move_count = sum(
                    is_within_board(new_x + mx, new_y + my) and board[new_y + my][new_x + mx] == -1
                    for mx, my in MOVES
                )
                possible_moves.append((move_count, (new_x, new_y)))

        if not possible_moves:
            return False

        x, y = min(possible_moves)[1]
        board[y][x] = step

    visualize_knights_tour(board)
    return True

def visualize_knights_tour(board):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(0.5, BOARD_SIZE, 1))
    ax.set_yticks(np.arange(0.5, BOARD_SIZE, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(which="both")
    ax.imshow(board, cmap="plasma")

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != -1:
                ax.text(j, i, str(board[i][j]), ha="center", va="center", fontsize=8)

    pair_array = np.zeros((BOARD_SIZE * BOARD_SIZE, 2), dtype=int)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] != -1:
                pair_array[board[i][j] - 1] = (j, i)

    for k in range(len(pair_array) - 1):
        j, i = pair_array[k]
        next_j, next_i = pair_array[k + 1]
        ax.plot([j, next_j], [i, next_i], color='yellow')

    plt.show()

if __name__ == '__main__':
    while not generate_closed_tour():
        pass
