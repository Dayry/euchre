import random

class Deck:

    def __init__(self, card_list=None, joker=False):
        self.card_list = card_list
        self.cards = []
        self.reset()

    def draw_card(self):
        return self.cards.pop()

    def cards_left(self):
        return len(self.cards)
    
    def discard(self):
        pass
        # is this needed?

    def shuffle(self):
        random.shuffle(self.cards)

    # def find_card(self, num_suit, num_value):
    #     for i in range(0, len(self.cards) - 1):
    #         print(f"{self.cards[i].show_string()} {self.cards[i].suit} {self.cards[i].value}")
    #         if self.cards[i].num_suit == num_suit and self.cards[i].num_value == num_value:
    #             return i
        
    def reset(self):
        self.cards = []

        if self.card_list == "euchre":
            for s in range(1, 5):
                for v in range(7, 15):
                    self.cards.append(Card(s, v))
            return

        for s in range(1, 5):
            for v in range(1, 14):
                self.cards.append(Card(s, v))


class Card:

    def __init__(self, num_suit, num_value):
        self.num_suit = num_suit
        self.num_value = num_value
        self.suit, self.value = self._get_val_suit()

    def _get_val_suit(self):
        s = self.num_suit
        v = self.num_value
        suit = 0
        value = 0

        if s == 1:
            suit = "Hearts"
        elif s == 2:
            suit = "Diamonds"
        elif s == 3:
            suit = "Clubs"
        elif s == 4:
            suit = "Spades"
        else:
            print("Invalid suit number")

        if v == 1 or v == 14:
            value = "Ace"
        elif v == 2:
            value = "Two"
        elif v == 3:
            value = "Three"
        elif v == 4:
            value = "Four"
        elif v == 5:
            value = "Five"
        elif v == 6:
            value = "Six"
        elif v == 7:
            value = "Seven"
        elif v == 8:
            value = "Eight"
        elif v == 9:
            value = "Nine"
        elif v == 10:
            value = "Ten"
        elif v == 12:
            value = "Queen"
        elif v == 13:
            value = "King"
        else: # v == 11 or v == 15 or v == 16+:
            value = "Jack"

        return suit, value

    def show_string(self):
        return f"{self.value} of {self.suit}"