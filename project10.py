import math
import time


def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  
            return True
        if all([board[j][i] == player for j in range(3)]):  
            return True

  
    if all([board[i][i] == player for i in range(3)]):  
        return True
    if all([board[i][2-i] == player for i in range(3)]):  
        return True

    return False


def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing, alpha, beta):

    if check_winner(board, "O"):
        return 10 - depth

    if check_winner(board, "X"):
        return depth - 10
   
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
       
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
      
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best


def best_move(board):
    best_val = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    
    return move


def take_turn(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please select a number between 1 and 9.")
                continue
            row, col = divmod(move-1, 3)
            if board[row][col] != " ":
                print("That spot is already taken. Try again.")
                continue
            board[row][col] = player
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
        except IndexError:
            print("Invalid move. Please select a number between 1 and 9.")

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)] 
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:

        take_turn(board, "X")
        print_board(board)

        if check_winner(board, "X"):
            print("Player X wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break

   
        print("AI is thinking...")
        time.sleep(1)
        move = best_move(board)
        board[move[0]][move[1]] = "O"
        print(f"AI plays at position {move[0] * 3 + move[1] + 1}")
        print_board(board)

        if check_winner(board, "O"):
            print("Player O (AI) win1s!")
            break
        if is_full(board):
            print("It's a tie!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
