RESULT_COLOR = "color"
RESULT_NUMBER = "number"
RESULT_HIDE = "hide"


class Card:

    # Constructor
    def __init__(self, nC, nN):
        self.color = nC
        self.number = nN

    def __eq__(self, other):
        if self.number != other.number:
            return False
        if self.color != other.color:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def getBlackJackNumberOfCard(self):
        if self.number == 1:
            return 11
        elif self.number >= 10:
            return 10
        else:
            return self.number

    def getInfo(self, showall=False, hide=False):
        cardInfo = {RESULT_COLOR:self.color,RESULT_NUMBER:self.number,RESULT_HIDE:1 if hide else 0}
        if not showall and hide:
            cardInfo[RESULT_COLOR] = 0
            cardInfo[RESULT_NUMBER] = 0
        return cardInfo


