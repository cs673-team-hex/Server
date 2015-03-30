import json,log,constant, time
import roommanager

INFO_ROOMID = 'roomid'
INFO_USERID = 'userid'

def removeUser(roomid, userid):
	types = roommanager.getRoomType(roomid)
	if types == None:
		log.warning('quitroom: cannot find room type; roomid:%d'%(roomid))
		return False
	result = roommanager.quitRoom(types,roomid,userid)
	if not result:
		log.warning('quitroom: user is not in room; roomid:%d, userid:%d'%(roomid,userid))
		return False;
	log.info('quitroom: successful; roomid:%d, userid:%d'%(roomid,userid))
	return True

def verify(roomid,userid):
	if not (isinstance(roomid,int) and isinstance(userid,int)):
		return False
	return True

def quitroom(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	roomid = None
	userid = None
	if INFO_ROOMID in data and INFO_USERID in data:
		roomid = data[INFO_ROOMID]
		userid = data[INFO_USERID]
	else:
		log.warning('quitroom: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid,userid):
		log.warning('quitroom: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	success = removeUser(roomid,userid)
	if not success:
		statu = constant.STATUS_OPERATION_FAILED
		return statu,result
	return statu, result
	
