from random import sample


def card_generator():
    bingo_card = {
        'B': sample(range(1, 16), k=5),
        'I': sample(range(16, 31), k=5),
        'N': sample(range(31, 46), k=5),
        'G': sample(range(46, 61), k=5),
        'O': sample(range(61, 76), k=5)
    }

    return bingo_card

def show_card(card):
    for key in card.keys():
        print(f"{key:>5}", end='')
    print()
    for i in range(len(card)):
        for value in card.values():
            print(f"{value[i]:>5}", end='')
        print()

def main():
    card = card_generator()
    show_card(card)


if __name__ == '__main__':
    main()