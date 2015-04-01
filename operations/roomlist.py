import json,log,constant
import roommanager

INFO_PAGE = 'page'
INFO_NUMBER = 'num'
INFO_TYPE = 'type'
RESULT_ROOMS = 'rooms'

def getRoomList(page, num, types):
	rooms = []
	if roommanager.isEmpty(types):
		return None
	if not roommanager.verifyPage(page,num,types):
		log.warning('roomlist: page number exceeded; page:%d, num:%d, types:%d'%(page,num,types))
		return None
	for room in roommanager.getRoomList(page, num, types):
		rooms.append(room.toListDict())
	log.info('roomlist: successful; page:%d, num:%d, types:%d'%(page,num,types))
	return {RESULT_ROOMS:rooms}


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
	if INFO_PAGE in data and INFO_NUMBER in data and INFO_TYPE in data:
		page = data[INFO_PAGE]
		num = data[INFO_NUMBER]
		types = data[INFO_TYPE]
	else:
		log.warning('roomlist: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(page, num, types):
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	rooms = getRoomList(page, num, types)
	if not rooms:
		return statu, result
	return statu, rooms