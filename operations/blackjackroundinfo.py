import json,log,constant
import roommanager

INFO_ROOMID = 'roomid'
INFO_USERID = 'userid'
RESULT_MEMBERS = 'members'
RESULT_WAGER = 'wager'

def getRoundInfo(roomid,userid):
	room = roommanager.getRoom(roomid)
	if room == None:
		log.warning('blackjackroundinfo: cannot find room; roomid:%d'%(roomid))
		return None
	if room.round == None:
		log.warning('blackjackroundinfo: there is no round in room; roomid:%d'%(roomid))
		return None
	membersInfo = [room.round.getAIInfo(showall=room.status==room.STATUS_WAITING),room.creator.getInfo(room.types, userid)]
	for cuserid,member in room.members.items():
		membersInfo.append(member.getInfo(room.types, userid))
	log.info('blackjackroundinfo: successful; roomid:%d, userid:%d'%(roomid,userid))
	return {RESULT_MEMBERS:membersInfo,RESULT_WAGER:room.wager}


def verify(roomid,userid):
	if not (isinstance(roomid,int) and (isinstance(userid,int) or isinstance(userid,long))):
		log.warning('blackjackroundinfo: information invalid')
		return False
	return True

def blackjackroundinfo(data):
	statu = constant.STATUS_SUCCESS
	result = {}
	roomid = None
	userid = None
	if INFO_ROOMID in data and INFO_USERID in data:
		roomid = data[INFO_ROOMID]
		userid = data[INFO_USERID]
	else:
		log.warning('blackjackroundinfo: missing parameters')
		statu = constant.STATUS_PARAMETER_UNMATCHED
		return statu,result
	if not verify(roomid,userid):
		statu = constant.STATUS_INFORMATION_INVALID
		return statu,result
	result = getRoundInfo(roomid,userid)
	if not result:
		return constant.STATUS_OPERATION_FAILED, result
	return statu, result