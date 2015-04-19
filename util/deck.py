from random import shuffle
from card import Card

class Deck:

    # Constructor
    def __init__(self, cl = None):
        self.cardList = []
        if cl is None:
            self.RebuildDeck()
        else:
            for card in cl:
                self.cardList.append(Card(card.color,card.number))

    def RebuildDeck(self):
        del self.cardList[:]
        i = 1
        while i <= 4:
            j = 1
            while j <= 13:
                self.cardList.append(Card(i, j))
                j += 1
            i += 1
        self.Shuffle()

    def removeCard(self, card):
        for tmpcard in self.cardList:
            if tmpcard == card:
                self.cardList.remove(tmpcard)

    def getTopCard(self):
        card = self.cardList[0]
        self.cardList.remove(card)
        return card

    def getNumber(self):
        return len(self.cardList)

    def Shuffle(self):
        shuffle(self.cardList)

