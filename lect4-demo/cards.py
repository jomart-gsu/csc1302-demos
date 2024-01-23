import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        """
        Possible improvement: figure out how numeric representations map to "King", "Ace", etc.
            Right now we can print the eleven of clubs, which isn't a card.
        """
        return f"{self.value} {self.suit}"

    def __lt__(self, other):
        return self.value < other.value


class Deck:
    def __init__(self):
        self.cards = []
        for value in range(13):
            for suit in ["Hearts", "Clubs", "Spades", "Diamonds"]:
                self.cards.append(Card(value, suit))

        self.shuffle()

    def shuffle(self):
        """
        Possible improvement: add a flag that resets the deck (e.g. returns all 52 cards to it).
        """
        random.shuffle(self.cards)

    def next_card(self):
        """
        Possible improvement (exercise): make it so you can't get the next card if the deck is empty
            OR add a parameter that determines the behavior in that case. Maybe the deck should auto-reset itself?
        """
        return self.cards.pop()

