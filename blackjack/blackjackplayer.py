RESULT_POSITION = "position"
RESULT_STATUS = "userstatus"
RESULT_CARDS = "cards"

class BlackjackPlayer:

    def getCards(self):
        newCardArray = []
        for card,hide in self.cardArray:
            newCardArray.append(card)
        return newCardArray

    def addCard(self, cardNewCard, hide=False):
        self.cardArray.append((cardNewCard,hide))

    def reset(self):
        self.isDouble = False
        self.isSurrend = False
        self.isStand = False
        self.isHit = False
        self.isStart = False
        if self.cardArray is not None:
            del self.cardArray[:]

    def create(self, position=0):
        self.isDouble = False
        self.isSurrend = False
        self.isStand = False
        self.isHit = False
        self.isStart = False
        self.position = position
        self.cardArray = []

    def getStatus(self):
        if self.isSurrend:
            return 5
        if self.isDouble:
            return 4
        if self.isStand:
            return 3
        if self.isHit:
            return 2
        if self.isStart:
            return 1
        return 0

    def getInfo(self, showall=False):
        result = {}
        result[RESULT_POSITION] = self.position
        result[RESULT_STATUS] = self.getStatus()
        cardInfos = []
        for card,hide in self.cardArray:
            cardInfos.append(card.getInfo(showall=showall,hide=hide))
        result[RESULT_CARDS] = cardInfos
        return result