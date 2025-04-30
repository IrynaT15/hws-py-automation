import random


class Card:

    value_list = ["2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suit_list = ["Hearts", "Diamonds", "Spades", "Clubs"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} {self.suit}"


class CardsDeck:

    def __init__(self):
        self.deck_54 = self.compose_a_deck()

    def __str__(self):
        return ', '.join(str(c) for c in self.deck_54)

    def compose_a_deck(self):
        self.deck_52 = []
        for value in Card.value_list:
            for suit in Card.suit_list:
                self.deck_52.append(Card(value, suit))
        self.deck_54 = self.deck_52 + ["Jocker"] * 2
        return self.deck_54

    def shuffle(self):
        random.shuffle(self.deck_54)
        return self.deck_54

    def get(self, number):
        if 1 <= number <= 54:
            return f"Your card is {self.deck_54[number-1]}"
        else:
            return "Invalid card number"


card1 = Card(2, "hearts")

deck = CardsDeck()
print(deck)
deck.shuffle()
print(deck)
card_number = int(input('Choose a card from 54-card deck:'))
card = deck.get(card_number)
print(card)

card_number = int(input('Choose a card from 54-card deck:'))
card = deck.get(card_number)
print(card)
