import json,log,constant, time

INFO_TITLE = 'title'
INFO_NUM = 'number'
INFO_TYPE = 'type'
INFO_WAGER = 'wager'
RESULT_HISTORYIES = 'histories'
RESULT_TIME = 'roomid'

def getNewRoom(title, number, types, wager):
	histories = []
	for i in range((page-1)*num, page*num):
		result = {}
		result[RESULT_TIME] = time.time()*1000
		result[RESULT_ID] = '%010d'%((page-1)*num+i)
		result[RESULT_WINNING] = i%2
		result[RESULT_TYPE] = 1
		histories.append(result)
	return {RESULT_HISTORYIES:histories}

def verify(title, number, types, wager):
	if not (isinstance(title,unicode) and isinstance(number,int) \
	and isinstance(types,int) and isinstance(wager,int)):
		return False
	if types not in constant.GAME_TYPE:
		return False
	return True

def createroom(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	title = None
	number = None
	types = None
	wager = None
	if INFO_TITLE in data and INFO_NUM in data\
	and INFO_TYPE in data and INFO_WAGER in data:
		title = data[INFO_TITLE]
		number = data[INFO_NUM]
		types = data[INFO_TYPE]
		wager = data[INFO_WAGER]
	else:
		log.warning('createroom: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(title, number, types, wager):
		log.warning('createroom: information invalid')
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	return statu, getNewRoom(title, number, types, wager)
	
