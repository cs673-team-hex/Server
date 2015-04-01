import json,log,constant
import roommanager

INFO_ROOMID = 'roomid'

def getRoomInfo(roomid):
	room = roommanager.getRoom(roomid)
	if room == None:
		log.warning('roominfo: cannot find room; roomid:%d'%(roomid))
		return None
	log.info('roominfo: successful; roomid:%d'%(roomid))
	return room.toInfoDict()


def verify(roomid):
	if not isinstance(roomid,int):
		log.warning('roominfo: information invalid')
		return False
	return True

def roominfo(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	if INFO_ROOMID in data:
		roomid = data[INFO_ROOMID]
	else:
		log.warning('roominfo: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid):
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	result = getRoomInfo(roomid)
	if not result:
		return statu, result
	return statu, result