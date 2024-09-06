import random

def create_deck():
    SUITS = ['s', 'h', 'd', 'c']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    deck = [s + v for s in SUITS for v in VALUES]

    # for suit in SUITS:
    #     for value in VALUES:
    #         card = suit + value
    #         deck.append(card)

    return deck


def shuffle(deck):
    first_half = deck[:26]
    second_half = deck[26:]
    shuffled_deck = []

    for _ in range(3):
        for i in range(len(first_half)):
            shuffled_deck.append(first_half[i])
            shuffled_deck.append(second_half[i])

    return shuffled_deck


def main():
    standart_deck = create_deck()
    print(standart_deck)
    shuffled_deck = standart_deck[:]
    random.shuffle(shuffled_deck)
    print(shuffled_deck)

if __name__ == '__main__':
    main()

