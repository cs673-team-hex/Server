import json,log,constant, time
import roommanager

INFO_ROOMID = 'roomid'
INFO_USERID = 'userid'

def start(roomid, userid):
	room = roommanager.getRoom(roomid)
	if room == None:
		log.warning('startgame: cannot find room type; roomid:%d'%(roomid))
		return False
	result = room.start()
	if not result:
		log.warning('startgame: user is not in room; roomid:%d, userid:%d'%(roomid,userid))
		return False;
	log.info('startgame: successful; roomid:%d'%(roomid))
	return True

def verify(roomid,userid):
	if not (isinstance(roomid,int) and isinstance(userid,long)):
		return False
	if not roommanager.isCreator(roomid, userid):
		log.warning('startgame: is not creator; roomid:%d, creatorid:%d'%(roomid,userid))
		return False
	return True

def startgame(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	roomid = None
	userid = None
	if INFO_ROOMID in data and INFO_USERID in data:
		roomid = data[INFO_ROOMID]
		userid = data[INFO_USERID]
	else:
		log.warning('startgame: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid,userid):
		log.warning('startgame: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	success = start(roomid,userid)
	if not success:
		statu = constant.STATUS_OPERATION_FAILED
		return statu,result
	return statu, result
	
