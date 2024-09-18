class Cell:
    def __init__(self, number):
        self.symbol = ' '
        self.number = number
        self.is_occupied = False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def occupy_cell(self, cell_number, symbol):
        if not self.cells[cell_number + 1].is_occupied:
            self.cells[cell_number + 1].is_occupied = True
            self.cells[cell_number + 1].symbol = symbol

    def check_game_end(self):
        ...