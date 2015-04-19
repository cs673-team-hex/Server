from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
import database
import constant
from blackjack.blackjackplayer import BlackjackPlayer

Base = declarative_base()

RESULT_USERID = 'userid'
RESULT_NICKNAME = 'nickname'
RESULT_CREDIT = 'credit'
RESULT_RANK = 'rank'
RESULT_RECORDS = 'records'
RESULT_BALANCE = 'balance'
RESULT_FACTOR1 = 'factor1'
RESULT_FACTOR2 = 'factor2'
RESULT_FACTOR3 = 'factor3'

class User(Base, BlackjackPlayer):
	__tablename__ = 'Users'

	user_id = Column(Integer, primary_key=True)
	username = Column(String, unique=True)
	nickname = Column(String)
	password = Column(String)
	balance = Column(Float,default=0)
	credit = Column(Integer,default=0)
	factor1 = Column(Float,default=0)
	factor2 = Column(Float,default=0)
	factor3 = Column(Float,default=0)

	def updateMoney(self, money):
		pass

	def toDict(self):
		result = {}
		result[RESULT_USERID] = self.user_id
		result[RESULT_NICKNAME] = self.nickname
		result[RESULT_CREDIT] = self.credit
		result[RESULT_RANK] = database.session.query(User).filter(User.credit > self.credit).count()+1
		result[RESULT_BALANCE] = self.balance
		result[RESULT_FACTOR1] = self.factor1
		result[RESULT_FACTOR2] = self.factor2
		result[RESULT_FACTOR3] = self.factor3
		return result

	def getInfo(self, types, userid):
		result = {}
		if types == constant.GAME_TYPE_BLACKJACK:
			result = BlackjackPlayer.getInfo(self, showall=userid==self.user_id)
			result[RESULT_USERID] = self.user_id
		return result