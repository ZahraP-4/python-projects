# Card Dealer Simulation

import random


def main():
    rounds = int(input("How many rounds to deal cards? "))

    for _ in range(rounds):
        deck = create_deck()
        num_cards = int(input("\nHow many cards should I deal? "))
        deal_cards(deck, num_cards)


def create_deck() -> dict:
    deck = {
        'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
        '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
        '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
        '10 of Spades': 10, 'Jack of Spades': 10,
        'Queen of Spades': 10, 'King of Spades': 10,

        'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
        '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
        '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
        '10 of Hearts': 10, 'Jack of Hearts': 10,
        'Queen of Hearts': 10, 'King of Hearts': 10,

        'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
        '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
        '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
        '10 of Clubs': 10, 'Jack of Clubs': 10,
        'Queen of Clubs': 10, 'King of Clubs': 10,

        'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
        '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
        '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
        '10 of Diamonds': 10, 'Jack of Diamonds': 10,
        'Queen of Diamonds': 10, 'King of Diamonds': 10
    }
    return deck


def deal_cards(deck: dict, number: int) -> None:
    hand_value = 0

    if number > len(deck):
        number = len(deck)

    for _ in range(number):
        card = random.choice(list(deck.keys()))
        value = deck.pop(card)
        print(card)
        hand_value += value

    print("Value of this hand:", hand_value)


if __name__ == "__main__":
    main()
