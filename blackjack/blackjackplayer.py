RESULT_POSITION = "position"
RESULT_STATUS = "userstatus"
RESULT_CARDS = "cards"

class BlackjackPlayer:

    STATUS_WAITING = 0;
    STATUS_STARTED = 1;
    STATUS_HITTED = 2;
    STATUS_STAND = 3;
    STATUS_DOUBLE = 4;
    STATUS_SURRENDER = 5;


    def getCards(self):
        newCardArray = []
        for card,hide in self.cardArray:
            newCardArray.append(card)
        return newCardArray

    def addCard(self, cardNewCard, hide=False):
        self.cardArray.append((cardNewCard,hide))

    def reset(self):
        self.isDouble = False
        self.isSurrender = False
        self.isStand = False
        self.isHit = False
        self.isStart = False
        if self.cardArray is not None:
            del self.cardArray[:]

    def create(self, position=0):
        self.isDouble = False
        self.isSurrender = False
        self.isStand = False
        self.isHit = False
        self.isStart = False
        self.position = position
        self.cardArray = []

    def getStatus(self):
        if self.isSurrender:
            return BlackjackPlayer.STATUS_SURRENDER
        if self.isDouble:
            return BlackjackPlayer.STATUS_DOUBLE
        if self.isStand:
            return BlackjackPlayer.STATUS_STAND
        if self.isHit:
            return BlackjackPlayer.STATUS_HITTED
        if self.isStart:
            return BlackjackPlayer.STATUS_STARTED
        return BlackjackPlayer.STATUS_WAITING

    def getInfo(self, showall=False):
        result = {}
        result[RESULT_POSITION] = self.position
        result[RESULT_STATUS] = self.getStatus()
        cardInfos = []
        for card,hide in self.cardArray:
            cardInfos.append(card.getInfo(showall=showall,hide=hide))
        result[RESULT_CARDS] = cardInfos
        return result