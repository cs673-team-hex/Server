RESULT_POSITION = "position"
RESULT_STATUS = "userstatus"
RESULT_CARDS = "cards"

class BlackjackPlayer:

    def getCards(self):
        newCardArray = []
        for card,hide in self.cardArray:
            newCardArray.append(card)
        return newCardArray

    def printCardInHand(self):
        sb = ""
        for card in self.cardArray:
            sb = sb+card.printCard()+" "
        sb = sb+"Total Num: "
        sb = sb+str(BlackJackRule.GetMaxValueOfHand(cardArray=self.cardArray))
        return sb

    def addCard(self, cardNewCard, hide=False):
        self.cardArray.append((cardNewCard,hide))

    def reset(self):
        self.isDouble = False
        self.isSurrend = False
        self.isStand = False
        if self.cardArray is not None:
            del self.cardArray[:]

    def create(self, position=0):
        self.isDouble = False
        self.isSurrend = False
        self.isStand = False
        self.position = position
        self.cardArray = []

    def getStatus(self):
        if self.isSurrend:
            return 4
        if self.isDouble:
            return 3
        if self.isStand:
            return 2
        return 1

    def getInfo(self, showall=False):
        result = {}
        result[RESULT_POSITION] = self.position
        result[RESULT_STATUS] = self.getStatus()
        cardInfos = []
        for card,hide in self.cardArray:
            cardInfos.append(card.getInfo(showall=showall,hide=hide))
        result[RESULT_CARDS] = cardInfos
        return result