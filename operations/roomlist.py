import json,log,constant
import roommanager
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound
from util.user import User

INFO_PAGE = 'page'
INFO_NUMBER = 'num'
INFO_TYPE = 'type'
INFO_USERID = 'userid'
RESULT_ROOMS = 'rooms'
RESULT_MONEY = 'money'
RESULT_RANK = 'rank'

def getRoomList(page, num, types):
	rooms = []
	if roommanager.isEmpty(types):
		return {}
	if not roommanager.verifyPage(page,num,types):
		log.warning('roomlist: page number exceeded; page:%d, num:%d, types:%d'%(page,num,types))
		return {}
	for room in roommanager.getRoomList(page, num, types):
		rooms.append(room.toListDict())
	log.info('roomlist: successful; page:%d, num:%d, types:%d'%(page,num,types))
	return {RESULT_ROOMS:rooms}

def getUserInfo(userid):
	try:
		user = session.query(User).\
		filter(User.user_id==userid).one()
		return user.balance, user.getRank()
	except (MultipleResultsFound, NoResultFound) as e:
		log.warning('login: query user fail;\t'+str(e))
		return None

def verify(page, num, types):
	if not (isinstance(page,int) and isinstance(num,int) and types in constant.GAME_TYPES):
		log.warning('roomlist: information invalid')
		return False
	return True

def roomlist(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	page = None
	num = None
	types = None
	userid = None
	if INFO_PAGE in data and INFO_NUMBER in data \
	and INFO_TYPE in data and INFO_USERID in data:
		page = data[INFO_PAGE]
		num = data[INFO_NUMBER]
		types = data[INFO_TYPE]
		userid = data[INFO_USERID]
	else:
		log.warning('roomlist: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(page, num, types):
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	rooms = getRoomList(page, num, types)
	money, rank = getUserInfo(userid)
	rooms[RESULT_MONEY] = money
	rooms[RESULT_RANK] = rank
	return statu, rooms