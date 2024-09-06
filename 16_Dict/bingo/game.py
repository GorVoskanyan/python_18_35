from random import shuffle
from time import sleep

from card import card_generator, show_card
from check_card import check_row, check_column, check_main_diagonal, check_diagonal

def game_main_loop():
    card = card_generator()
    box = list(range(1, 76))
    shuffle(box)

    while True:
        lucky_number = box.pop()
        for value in card.values():
            if lucky_number in value:
                value[value.index(lucky_number)] = 0

        print(f'{lucky_number}'.center(25, '-'))
        show_card(card)
        sleep(2)
        print('-' * 25)

        if check_diagonal(card) or check_main_diagonal(card) \
            or check_row(card) or check_column(card):
            break

    print('Has a winning card'.center(25, '-'))


if __name__ == '__main__':
    game_main_loop()