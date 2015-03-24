from sqlalchemy import Column, Integer, String, Float, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from util.user import User
import json,log,constant

Base = declarative_base()

RESULT_TIME = 'time'
RESULT_RECORDID = 'recordid'
RESULT_USERID = 'userid'
RESULT_WINNING = 'winning'
RESULT_TYPE = 'type'
RESULT_FACTOR1 = 'factor1'
RESULT_FACTOR2 = 'factor2'

class Record(Base):
	__tablename__ = 'Records'

	_id = Column(Integer, primary_key=True)
	record_id = Column(Integer)
	user_id = Column(Integer)
	types = Column(Integer)
	time = Column(BIGINT)
	winning = Column(Integer)
	factor1 = Column(Float,default=0)
	factor2 = Column(Float,default=0)

	def __init__(self,record_id,user_id,types,winning):
		Base.__init__(self,record_id=record_id,user_id=user_id,types=types,winning=winning,time=int(round(time.time() * 1000)));


	def toDict(self):
		result = {}
		result[RESULT_TIME] = self.time
		result[RESULT_RECORDID] = self.record_id
		result[RESULT_USERID] = self.user_id
		result[RESULT_WINNING] = self.winning
		result[RESULT_TYPE] = self.types
		result[RESULT_FACTOR1] = self.factor1
		result[RESULT_FACTOR2] = self.factor2
		return result