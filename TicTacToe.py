import math

board = [" "] * 9

def display_board():
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def is_full():
    return all(space != " " for space in board)

def minimax(is_maximizing, alpha, beta):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_full():
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                eval = minimax(False, alpha, beta)
                board[i] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval

    else:
        min_eval = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                eval = minimax(True, alpha, beta)
                board[i] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval

def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False, -math.inf, math.inf)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

def play_game():
    print("Welcome to Tic Tac Toe!")
    display_board()

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
            else:
                print("Invalid move, try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")
            continue

        display_board()

        if check_winner("X"):
            print("Congratulations! You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        print("AI is making a move...")
        ai_move()
        display_board()

        if check_winner("O"):
            print("AI wins! Better luck next time.")
            break
        if is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
