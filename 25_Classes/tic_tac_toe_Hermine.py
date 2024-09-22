"""
Задача 6. Крестики-нолики
Что нужно сделать
Создайте программу, которая реализует игру «Крестики-нолики».

Для этого напишите:

1. Класс, который будет описывать поле игры.

class Board:

    #  Класс поля, который создаёт у себя экземпляры клетки.

    #  Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).

    #  Помимо этого, класс должен содержать методы:

    #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её состояние. Если состояние удалось изменить, метод возвращает True, иначе возвращается False.

    #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False. True — если один из игроков победил, False — если победителя нет.

2. Класс, который будет описывать одну клетку поля:

class Cell:

    #  Клетка, у которой есть значения:

    #  занята она или нет;

    #  номер клетки;

    #  символ, который клетка хранит (пустая, крестик, нолик).

3. Класс, который описывает поведение игрока:

class Player:

    #  У игрока может быть:

    #  имя,

    #  количество побед.

    #  Класс должен содержать метод:

    #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки). Введённый номер нужно обязательно проверить.

4. Класс, который управляет ходом игры:

class Game:

    # класс «Игры» содержит атрибуты:

    # состояние игры,

    # игроки,

    # поле.

    # А также методы:

    # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле, проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.

    # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или ничьей. Если игра завершена, метод возвращает True, иначе False.

    # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать играть. После каждой игры выводится текущий счёт игроков.
"""

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
            return True
        return False

    def display_board(self):
        for i in range(0, 7, 3):
            if i % 3 == 0:
                print('-' * 6)
            print(f"{self.cells[i].symbol}|{self.cells[i+1].symbol}|{self.cells[i+2].symbol}")

    def check_game_end(self):
        win_combs = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # cols
            [0, 4, 8], [2, 4, 6]    # diagonals
        ]

        for comb in win_combs:
            i = 0
            if self.cells[comb[i]] == self.cells[comb[i+1]] == self.cells[comb[i+2]] != ' ':
                return True
        return False


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.game_state = self.board.check_game_end()

    def one_round(self, player):
        cel_num = int(input('Enter cell num: '))
        if self.board.occupy_cell(cel_num):
            if self.board.check_game_end():
                return True
            return False
        else:
            print('Cell is already occupied')
            return False



board = Board()
board.display_board()