import json,log,constant, time
from util.transaction import Transaction
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound

INFO_USERID = 'userid'
INFO_PAGE = 'page'
INFO_NUM = 'num'
RESULT_HISTORYIES = 'histories'

def toDict(histories):
	historiesDict = []
	for transaction in histories:
		historiesDict.append(transaction.toDict())
	return {RESULT_HISTORYIES:historiesDict}

def getHistory(userid, page, num):
	try:
		histories = session.query(Transaction).filter(Transaction.user_id==userid).order_by(Transaction.time).all()
		if page*num <= len(histories):
			return toDict(histories[(page-1)*num:page*num])
		elif (page-1)*num >= len(histories):
			return None
		else:
			return toDict(histories[0:])
	except (NoResultFound) as e:
		return None

def verify(userid, page, num):
	if not (isinstance(userid,int) and isinstance(page,int) \
	and isinstance(num,int)):
		return False
	return True

def tranhistory(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	userid = None
	page = None
	num = None
	if INFO_USERID in data and INFO_PAGE in data\
	and INFO_NUM in data :
		userid = data[INFO_USERID]
		page = data[INFO_PAGE]
		num = data[INFO_NUM]
	else:
		log.warning('tranhistory: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(userid, page, num):
		log.warning('tranhistory: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getHistory(userid, page, num)
	
