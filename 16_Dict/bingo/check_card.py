from card import card_generator, show_card

def check_column(card):
    for value in card.values():
        if sum(value) == 0:
            return True
    return False

def check_row(card):

    for i in range(len(card)):
        row_sum = 0
        for value in card.values():
            row_sum += value[i]
        if row_sum == 0:
            return True
    return False

def check_main_diagonal(card):
    main_diagonal = 0
    i = 0
    for key in card.keys():
        main_diagonal += card[key][i]
        i += 1

    if main_diagonal == 0:
        return True
    return False

def check_diagonal(card):
    diagonal = 0
    i = -1
    for key in card.keys():
        diagonal += card[key][i]
        i -= 1
    if diagonal == 0:
        return True
    return False


def main():
    card = card_generator()
    show_card(card)
