from sqlalchemy import Column, Integer, String, Float, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
import json,log,constant,time

Base = declarative_base()


RESULT_TRANSACTIONID = 'transactionid'
RESULT_TIME = 'time'
RESULT_CARD = 'cardnumber'
RESULT_TYPE = 'type'
RESULT_AMOUNT = 'amount'

class Transaction(Base):
	__tablename__ = 'Transactions'

	transaction_id = Column(Integer, primary_key=True)
	card_number = Column(String, unique=True)
	amount = Column(Float)
	types = Column(Integer)
	time = Column(BIGINT)
	user_id = Column(Integer)

	def __init__(self,card_number,amount,types,user_id):
		Base.__init__(self,card_number=card_number,amount=amount,types=types,user_id=user_id,time=int(round(time.time() * 1000)));

	def toDict(self):
		result = {}
		result[RESULT_TRANSACTIONID] = self.transaction_id
		result[RESULT_TIME] = self.time
		result[RESULT_CARD] = self.card_number
		result[RESULT_TYPE] = self.user_id
		result[RESULT_AMOUNT] = self.amount
		return result