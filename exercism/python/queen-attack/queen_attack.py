import math


class Queen:
    row: int
    column: int

    def __init__(self, row, column):
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def is_same_row_or_column(self, another_queen):
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        return False

    def is_sharing_diagonal(self, another_queen):
        if math.fabs(self.row - another_queen.row) - math.fabs(self.column - another_queen.column) == 0:
            return True
        return False

    def are_queens_on_the_same_position(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

    def can_attack(self, another_queen):
        self.are_queens_on_the_same_position(another_queen)
        return self.is_same_row_or_column(another_queen) or self.is_sharing_diagonal(another_queen)
