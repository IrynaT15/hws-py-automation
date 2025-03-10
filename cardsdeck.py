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
        return f"{self.deck_54}"

    def compose_a_deck(self):
        self.deck_52 = []
        for i in range(len(Card.value_list)):
            for j in range(len(Card.suit_list)):
                card = [Card.value_list[i], Card.suit_list[j]]
                self.deck_52.append(card)
        self.deck_54 = self.deck_52 + ["Jocker"] * 2
        return self.deck_54

    def shuffle(self):
        random.shuffle(self.deck_54)
        return self.deck_54

    def get(self, card_number):
        number_list = list(range(1, 55))
        if card_number in number_list:
            return self.deck_54[card_number-1]
        else:
            return "Invalid card number"

card1 = Card(2, "hearts")

deck = CardsDeck()
print(deck)
print(deck.shuffle())
card_number = int(input('Выберите карту из колоды в 54 карты:'))
card = deck.get(card_number)
print(f"Your card is {card}")

card_number = int(input('Выберите карту из колоды в 54 карты:'))
card = deck.get(card_number)
print(f"Your card is {card}")


