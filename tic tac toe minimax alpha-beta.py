#Juego del gato implementando algoritmo minimax con poda alfa-beta
import random

def play_tic_tac_toe():
    c = [[' ' for _ in range(3)] for _ in range(3)]
    count = 0
    winner = 2

    fill_matrix(c)
    startingPlayer = random.randint(0, 1)

    while winner == 2 and count < 9:
        print_board(c)

        if count % 2 == startingPlayer:
            ia_random(c)
        else:
            get_best_move(c)

        winner = check_winner(c)
        count += 1

    print_board(c)

    if winner == 0:
        print("Win IA random")
    elif winner == 1:
        print("Win MiniMax")
    else:
        print("Empate")

def fill_matrix(c):
    for i in range(3):
        for j in range(3):
            c[i][j] = ' '

def ia_random(c):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if c[i][j] != 'X' and c[i][j] != 'O':
                available_moves.append((i, j))

    if available_moves:
        i, j = random.choice(available_moves)
        c[i][j] = 'X'

def print_board(c):
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(f" {c[i][j]} |", end="")
            else:
                print(f" {c[i][j]}  ", end="")
        if i < 2:
            print("\n-----------")
    print("\n\n")

def get_best_move(c):
    best_score = -100
    best_i, best_j = 0, 0

    for i in range(3):
        for j in range(3):
            if c[i][j] != 'X' and c[i][j] != 'O':
                tmp = c[i][j]
                c[i][j] = 'O'
                score = minimax(c, 0, False, -float('inf'), float('inf'))  
                c[i][j] = tmp
                if score > best_score:
                    best_score = score
                    best_i, best_j = i, j

    c[best_i][best_j] = 'O'


def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    if result != 2:
        if result == 0:
            return depth - 10
        elif result == 1:
            return 10 - depth

    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    tmp = board[i][j]
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = tmp
                    best_score = max(best_score, score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] != 'X' and board[i][j] != 'O':
                    tmp = board[i][j]
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = tmp
                    best_score = min(best_score, score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score
    
def check_winner(c):
    for i in range(3):
        if c[i][0] == c[i][1] == c[i][2]:
            if c[i][0] == 'X':
                return 0
            elif c[i][0] == 'O':
                return 1

        if c[0][i] == c[1][i] == c[2][i]:
            if c[0][i] == 'X':
                return 0
            elif c[0][i] == 'O':
                return 1

    if c[0][0] == c[1][1] == c[2][2]:
        if c[0][0] == 'X':
            return 0
        elif c[0][0] == 'O':
            return 1

    if c[0][2] == c[1][1] == c[2][0]:
        if c[0][2] == 'X':
            return 0
        elif c[0][2] == 'O':
            return 1

    return 2

play_tic_tac_toe()