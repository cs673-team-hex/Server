from blackjack import blackjackAI
from blackjack import blackjackrule

class BlackJackRound:

    def __init__(self, playerArray, deck, endCallBack, wager=10):
        self.playerArray = playerArray
        self.cardDeck = deck
        self.wager = wager
        self.index = 0
        self.currentPlayer = self.playerArray[0]
        self.AICardArray = []
        self.endCallBack = endCallBack
        self.AICardArray.append(deck.getTopCard())
        self.AICardArray.append(deck.getTopCard())
        self.sendFirstTwoCards(self.currentPlayer)

    def sendFirstTwoCards(self, player):
        player.addCard(self.cardDeck.getTopCard(), hide=True)
        player.addCard(self.cardDeck.getTopCard())

    def playerDouble(self, userid):
        if self.currentPlayer.user_id != userid:
            return False
        self.currentPlayer.isDouble = True
        return self.playerHit(userid)

    def playerSurrend(self, userid):
        if self.currentPlayer.user_id != userid:
            return False
        self.currentPlayer.isSurrender = True
        return self.playerStand(userid)

    def playerStand(self, userid):
        if self.currentPlayer.user_id != userid:
            return False
        self.currentPlayer.isStand = True
        if len(self.playerArray) - 1 == self.index:
            self.AIPhase()
        else:
            self.index += 1
            self.currentPlayer = self.playerArray[self.index]
            self.sendFirstTwoCards(self.currentPlayer)
        return True

    def playerHit(self, userid):
        if self.currentPlayer.user_id != userid:
            return False
        if not (self.currentPlayer.isStand or self.currentPlayer.isSurrend):
            self.currentPlayer.addCard(self.cardDeck.getTopCard())
            #  Check GameStatus
            if blackjackrule.isBust(self.currentPlayer.getCards()):
                return self.playerStand(userid)
            if self.currentPlayer.isDouble:
                return self.playerStand(userid)
            if blackjackrule.isFiveDragon(self.currentPlayer.getCards()):
                return self.playerStand(userid)
            return True
        return False

    def AIPhase(self):
        while blackjackrule.getMaxValueOfHand(self.AICardArray) < 17:
            self.AICardArray.append(self.cardDeck.getTopCard())
            if blackjackrule.isBust(self.AICardArray):
                self.roundEndByAI()
                return
        while blackjackAI.doMakeDecision(self.cardDeck, self.AICardArray, self.currentPlayer.getCards()):
            self.AICardArray.append(self.cardDeck.getTopCard())
            if blackjackrule.isBust(self.AICardArray):
                self.roundEndByAI()
                return
        self.roundEndByAI()

    def roundEndByAI(self):
        self.moneyAffairs()
        self.endCallBack()

    def moneyAffairs(self):
        for player in self.playerArray:
            if player.isSurrend:
                player.updateMoney(-self.wager / 2)
            elif blackjackrule.getBlackJackResult(player.getCards(), self.AICardArray) > 0:
                if player.isDouble:
                    player.updateMoney(-self.wager * 2)
                else:
                    player.updateMoney(-self.wager)
            else:
                if player.isDouble:
                    player.updateMoney(self.wager * 2)
                else:
                    player.updateMoney(self.wager)

    def clear(self):
        for player in self.playerArray:
            player.reset()
        del self.cardDeck
