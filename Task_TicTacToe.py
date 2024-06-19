import math

# Initialize the board
def init_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    print("Current board:")
    print("-------------")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")
        print("-------------")

# Check for a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[cell] == player for cell in condition) for condition in win_conditions)

# Check for a draw
def check_draw(board):
    return ' ' not in board

# Make a move
def make_move(board, position, player):
    board[position] = player

# Get available moves
def get_available_moves(board):
    return [i for i, cell in enumerate(board) if cell == ' ']

# Minimax algorithm to find the best move
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if check_winner(board, ai_player):
        return 1
    elif check_winner(board, human_player):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

# Find the best move for the AI
def best_move(board):
    best_score = -math.inf
    move = -1
    for available_move in get_available_moves(board):
        board[available_move] = ai_player
        score = minimax(board, 0, False)
        board[available_move] = ' '
        if score > best_score:
            best_score = score
            move = available_move
    return move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    board = init_board()
    current_player = human_player

    while True:
        print_board(board)
        if current_player == human_player:
            try:
                move = int(input(f"Your turn ({human_player}), enter your move (0-8): "))
                if board[move] != ' ':
                    print("Invalid move. Cell already taken. Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input. Enter a number between 0 and 8.")
                continue
            make_move(board, move, human_player)
        else:
            print(f"AI ({ai_player}) is making a move...")
            move = best_move(board)
            make_move(board, move, ai_player)

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = human_player if current_player == ai_player else ai_player

    rematch = input("Do you want a rematch? (y/n): ").strip().lower()
    if rematch == 'y':
        play_game()
    else:
        print("Thanks for playing!")

# Ask user to choose their symbol
human_player = input("Choose your symbol (X/O): ").strip().upper()
if human_player == 'O':
    ai_player = 'X'
else:
    ai_player = 'O'

# Start the game
play_game()