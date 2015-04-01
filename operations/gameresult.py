import json,log,constant
import roommanager
from util.user import User
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound

INFO_ROOMID = 'roomid'
INFO_RESULTS = 'results'
INFO_CREATORID = 'userid'
INFO_USERID = 'userid'
INFO_WINNING = 'winning'

def setResult(roomid, results):
	room = roommanager.getRoom(roomid)
	if room == None:
		log.warning('gameresult: cannot find room; roomid:%d'%roomid)
		return False
	if not room.end():
		log.warning('gameresult: room cannot end; roomid:%d'%roomid)
		return False
	for result in results:
		userid = result[INFO_USERID]
		winning = result[INFO_WINNING]
		try:
			user = session.query(User).filter(User.user_id==userid).one()
		except (MultipleResultsFound, NoResultFound) as e:
			log.warning('gameresult: query user fail;\t'+str(e))
		user.balance += winning
		try:
			session.update(user)
		except Exception as e:
			session.rollback()
			log.warning('gameresult: update user fail;\t'+str(e))
			return False
	session.commit()
	log.info('gameresult: successful; roomid:%d, results:%s'%(roomid,str(results)))
	return True


def verify(roomid, creatorid, results):
	if not (isinstance(roomid,int) and isinstance(results,list) and isinstance(creatorid,int)):
		log.warning('gameresult: information invalid')
		return False
	if not roommanager.isCreator(roomid, creatorid):
		log.warning('gameresult: is not creator; roomid:%d, creatorid:%d'%(roomid,creatorid))
		return False
	for result in results:
		if not (INFO_USERID in result and INFO_WINNING in result):
			log.warning('gameresult: missing parameters')
			return False
		userid = result[INFO_USERID]
		winning = result[INFO_WINNING]
		if not (isinstance(userid,int) and isinstance(winning,int)):
			log.warning('gameresult: information invalid')
			return False
	return True

def gameresult(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	roomid = None
	creatorid = None
	results = None
	if INFO_ROOMID in data and INFO_RESULTS in data and INFO_CREATORID in data:
		roomid = data[INFO_ROOMID]
		results = data[INFO_RESULTS]
		creatorid = data[INFO_CREATORID]
	else:
		log.warning('gameresult: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid, creatorid, results):
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	if not setResult(roomid, results):
		statu = constant.STATUS_OPERATION_FAILED
		return statu,result
	return statu, results