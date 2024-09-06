from card_generator import create_deck
from random import shuffle

def deal(players_quantity, card_per_players, shuffled_deck):
    # hands = []
    # for _ in  range(players_quantity):
    #     hand = []
    #     for _ in range(card_per_players):
    #         card = shuffled_deck.pop()
    #         hand.append(card)
    #     hands.append(hand)

    hands = [[] for _ in range(players_quantity)]

    for _ in range(card_per_players):
        for i in range(players_quantity):
            card = shuffled_deck.pop()
            hands[i].append(card)

    return hands

def main():
    shuffled_deck = create_deck()
    # __import__('random').shuflle(shuflled_deck)
    shuffle(shuffled_deck)
    print(shuffled_deck)
    hands = deal(players_quantity=6, card_per_players=2, shuffled_deck=shuffled_deck)
    print(hands)
    print(shuffled_deck)

if __name__ == '__main__':
    main()