from piece import Piece
from piece_color import PieceColor


class Bishop(Piece):
    def __init__(self, loc_x, locY, color):
        super().__init__(loc_x, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bB.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wB.svg"
    def check_squares(self, board):
        pass
