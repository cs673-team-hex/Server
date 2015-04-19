from blackjack import blackjackrule
from util.deck import Deck
 

def GetOpponentPointDistribution(cdBeforeGame, myCard, oppCard):
    mapOpp = {}
    nOppNum = len(oppCard)
    if cdBeforeGame.getNumber() < len(myCard) + nOppNum:
        return None
    tempDeck = Deck(cl=cdBeforeGame.cardList)
    for card in myCard:
        tempDeck.removeCard(card)
    for card in oppCard:
        if oppCard.index(card) != 0:
            tempDeck.removeCard(card)
    for card in tempDeck.cardList:
        oppCard.append(card)
        nMaxNumber = blackjackrule.getMaxValueOfHand(oppCard)
        oppCard.remove(card)
        if nMaxNumber not in mapOpp:
            mapOpp[nMaxNumber] = 1
        else:
            mapOpp[nMaxNumber] = mapOpp[nMaxNumber] + 1
    return mapOpp

def GetDistributionOfOwnNewCard(cdBeforeGame, myCard, oppCard):
    mapOwn = {}
    nOppNum = len(oppCard)
    if cdBeforeGame.getNumber() < len(myCard) + nOppNum:
        return None
    tempDeck = Deck(cl=cdBeforeGame.cardList)
    for card in myCard:
        tempDeck.removeCard(card)
    for card in tempDeck.cardList:
        myCard.append(card)
        nMaxNumber = blackjackrule.getMaxValueOfHand(myCard)
        if nMaxNumber not in mapOwn:
            mapOwn[nMaxNumber] = 1
        else:
            mapOwn[nMaxNumber] = mapOwn[nMaxNumber] + 1
        myCard.remove(card)
    return mapOwn

def GetDistributionOfOwn(cdBeforeGame, myCard, oppCard):
    if cdBeforeGame.getNumber() < len(myCard) + len(oppCard):
        return None
    nMaxNumber = blackjackrule.getMaxValueOfHand(myCard)
    mapOwn = {}
    mapOwn[nMaxNumber]= 100
    return mapOwn

def GetWinningPoss(myDist, oppDist):
    nMyWin = 0
    nOppWin = 0
    nDraw = 0
    nTotal = 0
    if myDist == None or len(myDist) == 0:
        print("Warning myDist is NULL")
        winArray = [0, 0, 1]
        return winArray
    if oppDist == None:
        print("Warning oppDist is NULL")
        # Every Move Goes to hell;
        winArray = [0, 1, 0]
        return winArray
    if len(myDist) == 0:
        # Every Move Goes to hell;
        print("Warning myDist size is 0")
        winArray = [0, 0, 1]
        return winArray
    if len(oppDist) == 0:
        # Every Move Goes to hell;
        print("Warning oppDist size is 0")
        winArray = [0, 1, 0]
        return winArray
    for myPoint in myDist:
        for oppPoint in oppDist:
            if myPoint == oppPoint:
                nDraw += myDist[myPoint] * oppDist[oppPoint]
            elif myPoint > oppPoint:
                nMyWin += myDist[myPoint] * oppDist[oppPoint]
            else:
                nOppWin += myDist[myPoint] * oppDist[oppPoint]
            nTotal += myDist[myPoint] * oppDist[oppPoint]
    resultArray = [float(nMyWin) / float(nTotal), float(nDraw) / float(nTotal), float(nOppWin) / float(nTotal)]
    return resultArray

def doMakeDecisionLevelSB(cdBeforeGame, myCard, oppCard):
    return random() < 0.5

def doMakeDecisionLevel0(cdBeforeGame, myCard, oppCard):
    if blackjackrule.GetMaxValueOfHand(myCard) < 18 and blackjackrule.GetMaxValueOfHand(myCard) != -1:
        return True
    else:
        return False

def doMakeDecisionLevel1(cdBeforeGame, myCard, oppCard):
    myTreeMap = GetDistributionOfOwnNewCard(cdBeforeGame, myCard, oppCard)
    myTreeMapWhenStop = GetDistributionOfOwn(cdBeforeGame, myCard, oppCard)
    oppTreeMap = GetOpponentPointDistribution(cdBeforeGame, myCard, oppCard)
    resultArray = GetWinningPoss(myTreeMap, oppTreeMap)
    resultWhenStop = GetWinningPoss(myTreeMapWhenStop, oppTreeMap)
    if (resultArray[0] - resultArray[2]) > (resultWhenStop[0] - resultWhenStop[2]):
        return True
    else:
        return False

def doMakeDecision(cdBeforeGame, myCard, oppCard,level=1):
    if level == 1:
        return doMakeDecisionLevel1(cdBeforeGame, myCard, oppCard)
    elif level == 0:
        return doMakeDecisionLevel0(cdBeforeGame, myCard, oppCard)
    else:
        return doMakeDecisionLevelSB(cdBeforeGame, myCard, oppCard)

