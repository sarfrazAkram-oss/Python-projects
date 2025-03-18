import pygame
import numpy as np
import sys
import math

pygame.init()

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
MY_BLUE = (0, 0, 255)
MY_BLACK = (0, 0, 0)
MY_RED = (255, 0, 0)
MY_YELLOW = (255, 255, 0)


size = (COLUMN_COUNT * SQUARESIZE, (ROW_COUNT + 1) * SQUARESIZE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Connect Four")


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, MY_BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, MY_BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, MY_RED, (int(c * SQUARESIZE + SQUARESIZE / 2), size[1] - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, MY_YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), size[1] - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    pygame.display.update()


def winning_move(board, piece):
   
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True
  
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True
 
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def is_draw(board):
    for c in range(COLUMN_COUNT):
        if board[ROW_COUNT - 1][c] == 0:
            return False
    return True


def main():
    board = create_board()
    game_over = False
    turn = 0

    draw_board(board)
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, MY_BLACK, (0, 0, size[0], SQUARESIZE))
                posx = event.pos[0]
                pygame.draw.circle(screen, MY_RED, (posx, int(SQUARESIZE / 2)), RADIUS)

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
              
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            draw_board(board)
                            pygame.time.wait(500)
                            print("Player 1 wins!!")
                            game_over = True

              
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            draw_board(board)
                            pygame.time.wait(500)
                            print("Player 2 wins!!")
                            game_over = True

                draw_board(board)

                if is_draw(board):
                    draw_board(board)
                    print("It's a draw!")
                    game_over = True

                turn += 1
                turn = turn % 2

if __name__ == "__main__":
    main()
