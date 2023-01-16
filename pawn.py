from direction import Direction
from move_type import MoveType
from piece import Piece
from piece_color import PieceColor


class Pawn(Piece):
    def __init__(self, loc_x, locY, color):
        super().__init__(loc_x, locY, color)
        if color == PieceColor.BLACK:
            self.spriteLoc = "Assets/bP.svg"
        elif color == PieceColor.WHITE:
            self.spriteLoc = "Assets/wP.svg"

    def check_squares(self, board):
        super().check_squares(board)
        super().look_direction(board, Direction.UP, False, MoveType.OCCUPY)
        super().look_direction(board, Direction.RIGHT_UP, False, MoveType.CAPTURE)
        super().look_direction(board, Direction.LEFT_UP, False, MoveType.CAPTURE)
