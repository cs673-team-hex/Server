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

def getRoomType(roomid):
	for types,rooms in DICT_TYPES_ROOM.items():
		for room in rooms:
			if roomid == room.roomid:
				return types
	return None

def quitRoom(types, roomid, userid):
	room = None
	for tmp in DICT_TYPES_ROOM[types]:
		if tmp.roomid == roomid:
			room = tmp
	if room == None:
		return False
	result = room.removeMember(userid)
	if not result:
		return False
	if room.creator == None:
		DICT_TYPES_ROOM[types].remove(room)
	return True 
