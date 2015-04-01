import json,log,constant
from util.user import User
from database import session

INFO_USERNAME = 'username'
INFO_PASSWORD = 'passwd'
INFO_NICKNAME = 'nickname'

def verify(username, password, nickname):
	if not (isinstance(username,unicode) and isinstance(password,unicode) \
		and isinstance(nickname,unicode) and len(password)==32):
		log.warning('signup: information invalid')
		return None
	new_user = User(username=username,nickname=nickname,password=password)
	try:
		session.add(new_user)
		session.commit()
	except Exception as e:
		session.rollback()
		log.warning('signup: insert user fail;\t'+str(e))
		return None
	log.info('signup: successful; userid:%d, username:%s, password:%s'%(new_user.user_id,username,password))
	return new_user

def signup(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	username = None
	password = None
	nickname = None
	if INFO_USERNAME in data and INFO_PASSWORD in data and INFO_NICKNAME in data:
		username = data[INFO_USERNAME]
		password = data[INFO_PASSWORD]
		nickname = data[INFO_NICKNAME]
	else:
		log.warning('signup: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	new_user = verify(username, password,nickname)
	if not new_user:
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, new_user.toDict()
	
