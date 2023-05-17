from abc import abstractmethod

from Move import Move
from Pieces.Piece import Piece
from Pieces.Rook import Rook


class King(Piece):

    def __init__(self, *args):
        super().__init__(args[0])
        self.value = 0
        if len(args) == 1:
            self.has_moved = False
        else:
            self.has_moved = args[1]

    def __str__(self):
        if self.color == Piece.WHITE:
            return '\u2654'
        else:
            return '\u265A'

    def clone(self):
        return King(self.color, self.has_moved)

    def get_moves(self, b, x, y):
        moves = []
        # N
        if self.is_valid(x, y + 1) and \
                (not b.get_tile(x, y + 1).is_occupied()
                 or (b.get_tile(x, y + 1).is_occupied() and b.get_tile(x,
                                                                       y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x, y + 1))
        # NE
        if self.is_valid(x + 1, y + 1) and \
                (not b.get_tile(x + 1, y + 1).is_occupied()
                 or (b.get_tile(x + 1, y + 1).is_occupied() and b.get_tile(x + 1,
                                                                           y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y + 1))
        # E
        if self.is_valid(x + 1, y) and \
                (not b.get_tile(x + 1, y).is_occupied()
                 or (b.get_tile(x + 1, y).is_occupied() and b.get_tile(x + 1,
                                                                       y).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y))
        # SE
        if self.is_valid(x + 1, y - 1) and \
                (not b.get_tile(x + 1, y - 1).is_occupied()
                 or (b.get_tile(x + 1, y - 1).is_occupied() and b.get_tile(x + 1,
                                                                           y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x + 1, y - 1))
        # S
        if self.is_valid(x, y - 1) and \
                (not b.get_tile(x, y - 1).is_occupied()
                 or (b.get_tile(x, y - 1).is_occupied() and b.get_tile(x,
                                                                       y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x, y - 1))
        # SW
        if self.is_valid(x - 1, y - 1) and \
                (not b.get_tile(x - 1, y - 1).is_occupied()
                 or (b.get_tile(x - 1, y - 1).is_occupied() and b.get_tile(x - 1,
                                                                           y - 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y - 1))
        # W
        if self.is_valid(x - 1, y) and \
                (not b.get_tile(x - 1, y).is_occupied()
                 or (b.get_tile(x - 1, y).is_occupied() and b.get_tile(x - 1,
                                                                       y).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y))
        # NW
        if self.is_valid(x - 1, y + 1) and \
                ((not b.get_tile(x - 1, y + 1).is_occupied())
                 or (b.get_tile(x - 1, y + 1).is_occupied() and b.get_tile(x - 1,
                                                                           y + 1).get_piece().get_color() != self.color)):
            moves.append(Move(x, y, x - 1, y + 1))

        if self.color == Piece.WHITE:
            if not self.has_moved and x == b.e and y == 1 - 1:
                if not b.get_tile(b.f, 1 - 1).is_occupied() and \
                        not b.get_tile(b.g, 1 - 1).is_occupied() and \
                        b.get_tile(b.h, 1 - 1).is_occupied() and \
                        isinstance(b.get_tile(b.h, 1 - 1).get_piece(), Rook):
                    moves.append(Move(x, y, x + 2, y))
            else:
                self.has_moved = True
        else:
            if not self.has_moved and x == b.e and y == 8 - 1:
                if not b.get_tile(b.f, 8 - 1).is_occupied() and \
                        not b.get_tile(b.g, 8 - 1).is_occupied() and \
                        b.get_tile(b.h, 8 - 1).is_occupied() and \
                        isinstance(b.get_tile(b.h, 8 - 1).get_piece(), Rook):
                    moves.append(Move(x, y, x + 2, y))
            else:
                self.has_moved = True
        return moves
