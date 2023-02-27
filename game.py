import random

class Game:
    def __init__(self):
        cards = [(a, b, c, d) for a in range(3) for b in range(3) for c in range(3) for d in range(3)]
        random.shuffle(cards)

        self.cards_in_play = cards[:12]
        self.deck = cards[12:]

        while self.no_sets() and self.add_cards(): pass
        
    def is_set(self, x, y, z):
        """
        Check if the cards in positions x, y, z form a set.
        """
        sizes = [len(set(indexes)) for indexes in zip(self.cards_in_play[x], self.cards_in_play[y], self.cards_in_play[z])]
        return not any(size == 2 for size in sizes)
        
    def no_sets(self):
        """
        Check if there is not a set among the current cards in play.
        """
        for x in range(2, len(self.cards_in_play)):
            for y in range(1, x):
                for z in range(0, y):
                    if self.is_set(x, y, z):
                        return False
        return True

    def add_cards(self, number=3):
        """
        Add the number of cards given into play from our deck.  Return True
        if there are enough cards that this action is successful.  Return
        False if there are not enough cards remaining in our deck.
        """
        if len(self.deck) < number:
            return False
        
        for i in range(len(self.cards_in_play)):
            if number == 0:
                self.cards_in_play = [card for card in self.cards_in_play if card]
                return True
            
            if self.cards_in_play[i] is None:
                self.cards_in_play[i] = self.deck[-1]
                self.deck = self.deck[:-1]
                number -= 1

        
        self.cards_in_play.extend(self.deck[-number:])
        self.deck = self.deck[:-number]
        return True

    def make_move(self, x, y, z):
        """
        If the cards in positions x, y, z in play form a set, remove them.
        Otherwise, don't remove them.  Return False if the game is over, and
        True otherwise.
        """
        if not self.is_set(x, y, z):
            return True

        x, y, z = sorted([x, y, z], reverse=True)

        if len(self.cards_in_play) <= 12 and len(self.deck) >= 3:
            self.cards_in_play[x] = self.deck[-1]
            self.cards_in_play[y] = self.deck[-2]
            self.cards_in_play[z] = self.deck[-3]
        else:
            del self.cards_in_play[x]
            del self.cards_in_play[y]
            del self.cards_in_play[z]

        self.deck = self.deck[:-3]

        if len(self.deck) == 0:
            return False

        while len(self.cards_in_play) < 12 and self.add_cards(): pass
        while self.no_sets() and self.add_cards(): pass

        return True

    def hint(self):
        for x in range(2, len(self.cards_in_play)):
            for y in range(1, x):
                for z in range(0, y):
                    if self.is_set(x, y, z):
                        return [x, y, z]
        return None
