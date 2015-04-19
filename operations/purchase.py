import json,log,constant
from util.transaction import Transaction
from util.user import User
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound

INFO_USERID = 'userid'
INFO_CARDNUMBER = 'cardnumber'
INFO_EXPIRE = 'expire'
INFO_SN = 'securitynumber'
INFO_AMOUNT = 'amount'

def verify(userid, cardnumber, expire, securitynumber, amount):
	print type(userid), type(cardnumber), type(expire), type(securitynumber), type(amount)
	if not ((isinstance(userid,int) or isinstance(userid,long)) and isinstance(cardnumber,unicode) \
	and isinstance(expire,unicode) and isinstance(securitynumber,int) and (isinstance(amount,float) or isinstance(amount,int))):
		return False
	return addAmount(userid,amount,cardnumber)

def addAmount(userid,amount,cardnumber):
	try:
		session.query(User).filter(User.user_id==userid).one()
		session.query(User).filter(User.user_id==userid).update({"balance": User.balance + amount}, synchronize_session='fetch')
	except (MultipleResultsFound, NoResultFound) as e:
		log.warning('purchase: user not found;\t'+str(e))
		return False
	new_transaction = Transaction(cardnumber,amount,constant.TRANSACTION_TYPE_PURCHASE,userid)
	try:
		session.add(new_transaction)
		session.commit()
	except Exception as e:
		session.rollback()
		log.warning('purchase: purchase failed;\t'+str(e))
		return False
	return True

def purchase(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	userid = None
	cardnumber = None
	expire = None
	sn = None
	amount = None
	if INFO_USERID in data and INFO_CARDNUMBER in data\
	and INFO_EXPIRE in data and INFO_SN in data and INFO_AMOUNT in data:
		userid = data[INFO_USERID]
		cardnumber = data[INFO_CARDNUMBER]
		expire = data[INFO_EXPIRE]
		sn = data[INFO_SN]
		amount = data[INFO_AMOUNT]
	else:
		log.warning('purchase: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(userid, cardnumber, expire, sn, amount):
		log.warning('purchase: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, result
	
