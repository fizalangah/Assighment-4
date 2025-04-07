import math

# Initialize board
board = [" " for _ in range(9)]

# Print board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Check for winner
def winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if board is full
def is_full():
    return " " not in board

# Human move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Spot already taken!")
        else:
            print("Invalid input. Try again.")

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Minimax algorithm
def minimax(board_state, depth, is_maximizing):
    if winner("O"):
        return 1
    elif winner("X"):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "O"
                score = minimax(board_state, depth + 1, False)
                board_state[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "X"
                score = minimax(board_state, depth + 1, True)
                board_state[i] = " "
                best_score = min(score, best_score)
        return best_score

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if winner("X"):
            print("You win! 🎉")
            break
        if is_full():
            print("It's a draw! 🤝")
            break

        print("Computer is making a move...")
        ai_move()
        print_board()
        if winner("O"):
            print("Computer wins! 💻")
            break
        if is_full():
            print("It's a draw! 🤝")
            break

# Run the game
if __name__ == "__main__":
    play_game()
