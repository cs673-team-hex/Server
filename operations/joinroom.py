import json,log,constant, time
import roommanager
from util.user import User
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound

INFO_ROOMID = 'roomid'
INFO_USERID = 'userid'

def join(roomid, userid):
	room = roommanager.getRoom(roomid)
	if room == None:
		log.warning('joinroom: cannot find room; roomid:%d'%(roomid))
		return False
	user = None
	try:
		user = session.query(User).filter(User.user_id==userid).one()
	except (MultipleResultsFound, NoResultFound) as e:
		log.warning('joinroom: user id error;\t'+ str(e))
		return None
	result = roommanager.joinRoom(roomid,user)
	if not result:
		log.warning('joinroom: user already in or room fulled; roomid:%d, userid:%d'%(roomid,userid))
		return False;
	log.info('joinroom: successful; roomid:%d, userid:%d'%(roomid,userid))
	return True

def verify(roomid,userid):
	if not (isinstance(roomid,int) and (isinstance(userid,long) or isinstance(userid,int))):
		return False
	return True

def joinroom(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	roomid = None
	userid = None
	if INFO_ROOMID in data and INFO_USERID in data:
		roomid = data[INFO_ROOMID]
		userid = data[INFO_USERID]
	else:
		log.warning('joinroom: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid,userid):
		log.warning('joinroom: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	if not join(roomid,userid):
		statu = constant.STATUS_OPERATION_FAILED
	return statu, result
	
