import constant
from util.room import Room

MAX_ROOM_SIZE = 100000
MAX_MEMBER_SIZE = 8

DICT_TYPES_ID = {constant.GAME_TYPE_BLACKJACK:1}
DICT_TYPES_ROOM = {constant.GAME_TYPE_BLACKJACK:[]}

def getRoomList(page, num, types):
	if types in DICT_TYPES_ROOM and (page-1)*num < len(DICT_TYPES_ROOM[types]):
		if page*num <= len(DICT_TYPES_ROOM[types]):
			return DICT_TYPES_ROOM[types][(page-1)*num:(page-1)*num+num]
		else:
			return DICT_TYPES_ROOM[types][(page-1)*num:]
	return None

def createRoom(title, max_number, types, creatorid, wager=10):
	if max_number > MAX_MEMBER_SIZE or max_number<=0:
		return None
	if types in DICT_TYPES_ID:
		roomid = DICT_TYPES_ID[types]*MAX_ROOM_SIZE+len(DICT_TYPES_ROOM[types])
		room = Room(roomid, title, max_number, types, creatorid, wager=wager)
		DICT_TYPES_ROOM[types].append(room)
		return roomid
	return None

def verifyPage(page, num, types):
	if (page-1)*num >= len(DICT_TYPES_ROOM[types]):
		return False
	return True

def isEmpty(types):
	return len(DICT_TYPES_ROOM[types])==0

def quitRoom(roomid, userid):
	room = getRoom(roomid)
	if room == None:
		return False
	result = room.removeMember(userid)
	if not result:
		return False
	if room.creator == None:
		DICT_TYPES_ROOM[room.types].remove(room)
	return True 

def isCreator(roomid, creatorid):
	room = getRoom(roomid)
	if room == None:
		return False
	return room.creator.user_id == creatorid

def getRoom(roomid):
	for types in DICT_TYPES_ROOM: 
		for room in DICT_TYPES_ROOM[types]:
			if room.roomid == roomid:
				return room
	return None