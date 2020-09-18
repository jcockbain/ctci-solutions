import unittest
import random


class Card:
    SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANKS = (
        "narf",
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    )

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} of {1}".format(Card.RANKS[self.rank], Card.SUITS[self.suit])


class Deck:
    def __init__(self, cards=[]):
        self.cards = cards

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            print(card)


class BlackjackHand(Deck):
    def value(self):
        value = 0
        for card in self.cards:
            value += min(card.rank, 10)
        return value


class Test(unittest.TestCase):
    def test_deck_of_cards(self):
        deck = BlackjackHand([Card(2, 5), Card(2, 11)])
        self.assertEqual(15, deck.value())
