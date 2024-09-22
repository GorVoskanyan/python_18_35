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
        if not self.cells[cell_number - 1].is_occupied:
            self.cells[cell_number - 1].is_occupied = True
            self.cells[cell_number - 1].symbol = symbol
            return True
        return False

    def display_board(self):
        for i in range(0, 9, 3):
            print('-' * 9)
            print(f"{self.cells[i].symbol} | {self.cells[i+1].symbol} | {self.cells[i+2].symbol}")
        print('-' * 9)

    def check_game_end(self):
        win_combs = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]

        for comb in win_combs:
            if self.cells[comb[0]].symbol == self.cells[comb[1]].symbol == self.cells[comb[2]].symbol != ' ':
                return True
        return False

    def is_board_full(self):
        return all(cell.is_occupied for cell in self.cells)


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = self.player1

    def one_round(self):
        self.board.display_board()
        cell_num = int(input(f'{self.current_player.name}, enter cell num (1-9): '))
        if self.board.occupy_cell(cell_num, self.current_player.symbol):
            if self.board.check_game_end():
                print(f'{self.current_player.name} wins!')
                self.board.display_board()
                return True
            elif self.board.is_board_full():
                print("It's a draw!")
                self.board.display_board()
                return True
            self.switch_player()
            return False
        else:
            print('Cell is already occupied')
            return False

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def start_game(self):
        game_ended = False
        while not game_ended:
            game_ended = self.one_round()

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            self.board = Board()  # նորից սկսում ենք դաշտը
            self.start_game()      # նորից սկսում ենք խաղը



player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")

game = Game(player1, player2)
game.start_game()
