import log,constant
import roommanager
import util

INFO_ROOMID = 'roomid'
INFO_USERID = 'userid'
INFO_OPERATION = 'opt'

OPERATION_HIT = 1
OPERATION_STAND = 2
OPERATION_DOUBLE = 3
OPERATION_SURREND = 4

def operate(roomid, userid,operation):
	room = roommanager.getRoom(roomid)
	if room == None:
		log.warning('blackjackhandler: cannot find room; roomid:%d'%(roomid))
		return False
	if room.status != util.room.Room.STATUS_STARTED or room.round == None:
		log.warning('blackjackhandler: room not start; roomid:%d'%(roomid))
		return False
	if operation == OPERATION_HIT:
		return room.round.playerHit(userid)
	elif operation == OPERATION_DOUBLE:
		return room.round.playerDouble(userid)
	elif operation == OPERATION_STAND:
		return room.round.playerStand(userid)
	elif operation == OPERATION_SURREND:
		return room.round.playerSurrend(userid)
	log.warning('blackjackhandler: operation unsupported; operation:%d'%(operation))
	return False

def verify(roomid,userid,operation):
	if not (isinstance(roomid,int) and isinstance(operation,int)\
		and (isinstance(userid,long) or isinstance(userid,int))):
		return False
	if not roommanager.isInRoom(roomid, userid):
		log.warning('blackjackhandler: is not in room; roomid:%d, creatorid:%d'%(roomid,userid))
		return False
	return True

def blackjackhandler(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	roomid = None
	userid = None
	operation = None
	if INFO_ROOMID in data and INFO_USERID in data and INFO_OPERATION in data:
		roomid = data[INFO_ROOMID]
		userid = data[INFO_USERID]
		operation = data[INFO_OPERATION]
	else:
		log.warning('blackjackhandler: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid,userid,operation):
		log.warning('blackjackhandler: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	if not operate(roomid,userid,operation):
		statu = constant.STATUS_OPERATION_FAILED
		return statu,result
	return statu, result
	