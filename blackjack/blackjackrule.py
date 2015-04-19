def isBlackJack(cardArray):
    if cardArray is not None:
        if len(cardArray) != 2:
        # You certainly not, Man!
            return False
        if cardArray[0].number == 1 and cardArray[1].number >= 10 and cardArray[1].number < 12:
            return True
        if cardArray[1].number == 1 and cardArray[0].number >= 10 and cardArray[0].number < 12:
            return True
    return False

def isFiveDragon(cardArray):
    if cardArray is not None:
        if len(cardArray) >= 5 and getMaxValueOfHand(cardArray) != -1:
            return True
    return False

def isBust(cardArray):
    if cardArray is not None:
        return getMaxValueOfHand(cardArray) == -1
    return False

def getMaxValueOfHand(cardArray):
    if cardArray is not None:
        nNumOfAce = 0
        nTotal = 0
        for card in cardArray:
            nTotal += card.getBlackJackNumberOfCard()
            if card.getBlackJackNumberOfCard() == 11:
                nNumOfAce += 1
        if nTotal <= 21:
            return nTotal
        elif nTotal > 21 and nNumOfAce == 0:
            return -1
        elif nNumOfAce == 0:
            return nTotal
        else:
            # Total > 21 and there is on more A
            i = 0
            while i < nNumOfAce:
                nTotal -= 10
                if nTotal <= 21:
                    return nTotal
                i += 1
            #  Could not happen but need some log
            return -1

def getBlackJackResult(playerCardArray, AICardArray):
    nRet = 0
    if isBlackJack(AICardArray):
        nRet = 10
    elif isBlackJack(playerCardArray):
        nRet = -10
    elif isFiveDragon(AICardArray):
        nRet = 20
    elif isFiveDragon(playerCardArray):
        nRet = -20
    elif getMaxValueOfHand(playerCardArray) <= getMaxValueOfHand(AICardArray):
        nRet = 30
    else:
        nRet = -30
    return nRet