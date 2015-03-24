import json,log,constant
from util.user import User
from database import session
from sqlalchemy.orm.exc import MultipleResultsFound,NoResultFound

INFO_USERNAME = 'username'
INFO_PASSWORD = 'passwd'


def verify(username, password):
	if not (isinstance(username,int) and isinstance(password,unicode) and len(password)==32):
		log.warning('login: information invalid')
		return None
	try:
		user = session.query(User).\
		filter(User.username==username, User.password==password).one()
		return user
	except (MultipleResultsFound, NoResultFound) as e:
		log.warning('login: query user fail;\t'+str(e))
		return None
	return None

def login(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	username = None
	password = None
	if INFO_USERNAME in data and INFO_PASSWORD in data:
		username = data[INFO_USERNAME]
		password = data[INFO_PASSWORD]
	else:
		log.warning('login: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	user = verify(username, password)
	if not user:
		log.warning('login: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, user.toDict()
	
