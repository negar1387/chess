import pygame
from pygame.locals import *


class ChessGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 850 # عرض پنجره
        self.screen_height = 770 # ارتفاع پنجره
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Chess Game")
        self.board_offset = (100, 100)
        self.square_size = 55
        self.selected_piece = None
        self.chess_board = ChessBoard()
        self.draw_chessboard()
        self.load_pieces()
        self.draw_pieces()

    def draw_chessboard(self):
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        square_size = 10
        for row in range(12):
            for col in range(12):
                x = col * self.square_size + self.board_offset[0]
                y = row * self.square_size + self.board_offset[1]
                if (row + col) % 2 == 0:
                    color = RED
                else:
                    color = GREEN
                pygame.draw.rect(self.screen, color, (x, y, self.square_size, self.square_size))

    def load_pieces(self):
        self.piece_images = {
            "R": pygame.transform.scale(pygame.image.load("./images/rook.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "N": pygame.transform.scale(pygame.image.load("images/knight.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "C": pygame.transform.scale(pygame.image.load("images/catapult.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "B": pygame.transform.scale(pygame.image.load("images/bishop.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "Q": pygame.transform.scale(pygame.image.load("images/queen.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "K": pygame.transform.scale(pygame.image.load("images/king.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "P": pygame.transform.scale(pygame.image.load("images/pawn.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "S": pygame.transform.scale(pygame.image.load("images/Sergeant.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "r": pygame.transform.scale(pygame.image.load("images/black rook.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "n": pygame.transform.scale(pygame.image.load("images/black knight.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "c": pygame.transform.scale(pygame.image.load("images/black catapult.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "b": pygame.transform.scale(pygame.image.load("images/black bishop.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "q": pygame.transform.scale(pygame.image.load("images/black queen.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "k": pygame.transform.scale(pygame.image.load("images/black king.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "p": pygame.transform.scale(pygame.image.load("images/black pawn.png").convert(), (self.square_size // 2, self.square_size // 2)),
            "s": pygame.transform.scale(pygame.image.load("images/black Sergeant.png").convert(), (self.square_size // 2, self.square_size // 2))
        }

        for piece in self.piece_images.values():
            piece.set_colorkey((0, 0, 0))

    def draw_pieces(self):
        piece_positions = [
            ["R", "C", "-", "K", "Q", "-", "C", "R", "P", "-", "-", "-"],
            ["-", "N", "B", "-", "-", "B", "N", "P", "-", "-", "-", "-"],
            ["-", "-", "S", "S", "S", "-", "P", "-", "-", "-", "-", "-"],
            ["P", "P", "P", "P", "P", "P", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "p", "p", "p", "p", "p", "p"],
            ["-", "-", "-", "-", "-", "p", "-", "s", "s", "s", "-", "-"],
            ["-", "-", "-", "-", "p", "n", "b", "-", "-", "b", "n", "-"],
            ["-", "-", "-", "p", "r", "c", "-", "q", "k", "-", "c", "r"]
        ]
        for row in range(12):
            for col in range(12):
                piece = piece_positions[row][col]
                if piece != "-":
                    image = self.piece_images[piece]
                    x = col * self.square_size + self.board_offset[0]+ self.square_size // 2
                    y = row * self.square_size + self.board_offset[1]+ self.square_size // 2
                    image_rect = image.get_rect(center=(x, y))
                    self.screen.blit(image, image_rect)

def start(self):
    running = True
    clock = pygame.time.Clock()  # ساخت یک شیء از clock برای مدیریت فریم‌ها
    while running:
        clock.tick(60)  # تنظیم نرخ فریم به 60 فریم در ثانیه
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                board_x = (mouse_x - self.board_offset[0]) // self.square_size
                board_y = (mouse_y - self.board_offset[1]) // self.square_size
                if self.selected_piece is None:
                    self.selected_piece = self.chess_board.board[board_y][board_x]
                else:
                    if self.is_valid_move(self.selected_piece, (board_y, board_x), self.chess_board):
                        print("Move successful!")
                        self.draw_chessboard()
                        self.draw_pieces()
                        pygame.display.flip()
                    else:
                        print("Invalid move!")
                    self.selected_piece = None

            else:
                print("Invalid move!")

    def is_valid_move(self, piece, move, board):
        
        if piece and move in piece.get_valid_moves():
            old_position = (piece.row, piece.col)
            new_position = move
            piece.move(*new_position)
            board.board[old_position[0]][old_position[1]] = None
            board.board[new_position[0]][new_position[1]] = piece
            return True
        else:
            print("Invalid move! Please try again.")
            return False


class ChessBoard:
    def __init__(self):
        self.board = [
            ["r", "c", "-", "k", "q", "-", "c", "r", "p", "-", "-", "-"],
            ["-", "n", "b", "-", "-", "b", "n", "p", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "p", "-", "-", "-", "-", "-"],
            ["p", "p", "p", "p", "p", "p", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "p", "p", "p", "p", "p", "p"],
            ["-", "-", "-", "-", "-", "p", "-", "s", "s", "s", "-", "-"],
            ["-", "-", "-", "-", "p", "n", "b", "-", "-", "b", "n", "-"],
            ["-", "-", "-", "p", "r", "c", "-", "q", "k", "-", "c", "r"]
        ]



class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.is_alive = True

    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

    def capture(self):
        self.is_alive = False


class Pawn(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.has_moved = False
        self.symbol = 'P'

    def move(self, new_row, new_col):
        if not self.has_moved:
            if (new_row == self.row + 1 or new_row == self.row + 2) and new_col == self.col:
                self.row = new_row
                self.col = new_col
                self.has_moved = True
            else:
                print("Invalid move for Pawn!")
                return
        elif new_row == self.row + 1 and new_col == self.col:
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid move for Pawn!")
            return


class Sergeant(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.type = "Sergeant"

    def get_valid_moves(self):
        valid_moves = []
        if self.color == "white":
            # حرکت به جلو
            if self.row > 0:
                valid_moves.append((self.row - 1, self.col))
                if self.row > 1:  # حرکت دو خانه به جلو
                    valid_moves.append((self.row - 2, self.col))

                # حرکت برای زدن به صورت مورب به راست بالا
                if self.col < 11 and self.row > 0:
                    valid_moves.append((self.row - 1, self.col + 1))

                # حرکت برای زدن به صورت مورب به چپ بالا
                if self.col > 0 and self.row > 0:
                    valid_moves.append((self.row - 1, self.col - 1))

        else:  # برای مهره‌های سیاه
            # حرکت به جلو
            if self.row < 11:
                valid_moves.append((self.row + 1, self.col))
                if self.row < 10:  # حرکت دو خانه به جلو
                    valid_moves.append((self.row + 2, self.col))

                # حرکت برای زدن به صورت مورب به راست پایین
                if self.col < 11 and self.row < 11:
                    valid_moves.append((self.row + 1, self.col + 1))

                # حرکت برای زدن به صورت مورب به چپ پایین
                if self.col > 0 and self.row < 11:
                    valid_moves.append((self.row + 1, self.col - 1))

        return valid_moves


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = 'B'

    def move(self, new_row, new_col):
        if abs(new_row - self.row) == abs(new_col - self.col):
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid move for Bishop!")

    def get_valid_moves(self):
        valid_moves = []
        for i in range(1, 12):
            if self.row + i < 12 and self.col + i < 12:
                valid_moves.append((self.row + i, self.col + i))
            if self.row + i < 12 and self.col - i >= 0:
                valid_moves.append((self.row + i, self.col - i))
            if self.row - i >= 0 and self.col + i < 12:
                valid_moves.append((self.row - i, self.col + i))
            if self.row - i >= 0 and self.col - i >= 0:
                valid_moves.append((self.row - i, self.col - i))
        return valid_moves


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = 'N'

    def move(self, new_row, new_col):
        row_diff = abs(new_row - self.row)
        col_diff = abs(new_col - self.col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid move for Knight!")

    def get_valid_moves(self):
        valid_moves = []
        possible_moves = [
            (self.row + 2, self.col + 1),
            (self.row + 2, self.col - 1),
            (self.row - 2, self.col + 1),
            (self.row - 2, self.col - 1),
            (self.row + 1, self.col + 2),
            (self.row + 1, self.col - 2),
            (self.row - 1, self.col + 2),
            (self.row - 1, self.col - 2)
        ]
        for move in possible_moves:
            if 0 <= move[0] < 12 and 0 <= move[1] < 12:
                valid_moves.append(move)
        return valid_moves


class Catapult(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = 'C'

    def move(self, new_row, new_col):
        row_diff = abs(new_row - self.row)
        col_diff = abs(new_col - self.col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2) or \
           (row_diff == 1 and col_diff == 1):
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid move for Catapult!")

    def get_valid_moves(self):
        valid_moves = []
        possible_moves = [
            (self.row + 2, self.col + 1),
            (self.row + 2, self.col - 1),
            (self.row - 2, self.col + 1),
            (self.row - 2, self.col - 1),
            (self.row + 1, self.col + 2),
            (self.row + 1, self.col - 2),
            (self.row - 1, self.col + 2),
            (self.row - 1, self.col - 2),
            (self.row + 1, self.col + 1),
            (self.row + 1, self.col - 1),
            (self.row - 1, self.col + 1),
            (self.row - 1, self.col - 1)
        ]
        for move in possible_moves:
            if 0 <= move[0] < 12 and 0 <= move[1] < 12:
                valid_moves.append(move)
        return valid_moves


class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = 'R'

    def move(self, new_row, new_col):
        if new_row == self.row or new_col == self.col:
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid move for Rook!")

    def get_valid_moves(self):
        valid_moves = []
        for i in range(self.row + 1, 12):
            valid_moves.append((i, self.col))
        for i in range(self.row - 1, -1, -1):
            valid_moves.append((i, self.col))
        for i in range(self.col + 1, 12):
            valid_moves.append((self.row, i))
        for i in range(self.col - 1, -1, -1):
            valid_moves.append((self.row, i))
        return valid_moves


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = 'Q'

    def move(self, new_row, new_col):
        if new_row == self.row or new_col == self.col or abs(new_row - self.row) == abs(new_col - self.col):
            self.row = new_row
            self.col = new_col
        else:
            print("Invalid move for Queen!")

    def get_valid_moves(self):
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for direction in directions:
            row, col = self.row, self.col
            while True:
                row += direction[0]
                col += direction[1]
                if 0 <= row < 12 and 0 <= col < 12:
                    valid_moves.append((row, col))
                else:
                    break
        return valid_moves


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.symbol = 'K'

    def move(self, new_row, new_col):
        if abs(new_row - self.row) <= 1 and abs(new_col - self.col) <= 1:
            self.row = new_row
            self.col = new_col
            return True
        else:
            print("Invalid move for King!")
            return False

    def get_valid_moves(self):
        valid_moves = []
        possible_moves = [
            (self.row + 1, self.col),
            (self.row - 1, self.col),
            (self.row, self.col + 1),
            (self.row, self.col - 1),
            (self.row + 1, self.col + 1),
            (self.row + 1, self.col - 1),
            (self.row - 1, self.col + 1),
            (self.row - 1, self.col - 1)
        ]
        for move in possible_moves:
            if 0 <= move[0] < 12 and 0 <= move[1] < 12:
                valid_moves.append(move)
        return valid_moves


# Start the game
game = ChessGame()
pygame.display.flip()


quit=input()


#delete the source code of full screen



