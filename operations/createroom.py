import json,log,constant, time
import roommanager
from util.user import User
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound

INFO_TITLE = 'title'
INFO_NUM = 'number'
INFO_TYPE = 'type'
INFO_WAGER = 'wager'
INFO_USERID = 'userid'
RESULT_ROOMID = 'roomid'

def getNewRoom(title, number, types, userid, wager):
	user = None
	try:
		user = session.query(User).filter(User.user_id==userid).one()
	except (MultipleResultsFound, NoResultFound) as e:
		log.warning('createroom: creator id error;\t'+ str(e))
		return None
	roomid = roommanager.createRoom(title, number, types, user, wager=wager)
	if roomid == None:
		log.warning('createroom: room is full; type:%d'%(types))
		return None
	else:
		log.warning('createroom: successful; roomid:%d'%(roomid))
		return {RESULT_ROOMID:roomid}

def verify(title, number, types, wager, userid):
	if not (isinstance(title,unicode) and isinstance(number,int) and isinstance(types,int) \
		and isinstance(wager,int) and (isinstance(userid, long) or isinstance(userid, int))):
		return False
	if types not in constant.GAME_TYPES:
		return False
	return True

def createroom(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	if INFO_TITLE in data and INFO_NUM in data and INFO_USERID in data \
	and INFO_TYPE in data and INFO_WAGER in data:
		title = data[INFO_TITLE]
		number = data[INFO_NUM]
		types = data[INFO_TYPE]
		wager = data[INFO_WAGER]
		userid = data[INFO_USERID]
	else:
		log.warning('createroom: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(title, number, types, wager, userid):
		log.warning('createroom: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	result = getNewRoom(title, number, types, userid, wager)
	if result == None:
		log.warning('createroom: create room failed')
		statu = constant.STATUS_OPERATION_FAILED
		return statu,result
	return statu, result
	
