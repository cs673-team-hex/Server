import json,log,constant
from util.user import User
from database import session

RESULT_ROOMID = 'roomid'
RESULT_TITLE = 'title'
RESULT_MAX_NUMBER = 'mnumber'
RESULT_CURRENT_NUMBER = 'cnumber'
RESULT_TYPES = 'type'
RESULT_WAGER = 'wager'
RESULT_STATUS = 'roomstatus'
RESULT_NICKNAME = 'nickname'
RESULT_USERID = 'userid'
RESULT_MEMBERS = 'members'

STATUS_WAITING = 1
STATUS_STARTED = 2

class Room:
	roomid = None
	title = None
	max_number = None
	types = None
	wager = None
	status = None
	creator = None
	members = {}

	def __init__(self, roomid, title, max_number, types, creator, wager=10):
		self.roomid = roomid
		self.status = STATUS_WAITING
		self.title = title
		self.max_number = max_number
		self.types = types
		self.wager = wager
		self.creator = creator

	def addMember(self, member):
		if len(members)>=max_number-1:
			return False
		if member.user_id == self.creator.user_id:
			return False
		if member.user_id in members:
			return False
		members[member.user_id] = member
		return True

	def removeMember(self, memberid):
		if memberid == self.creator.user_id:
			del self.creator
			self.creator = None
			return True
		if memberid in selfmembers:
			members.remove(memberid)
			return True
		return False

	def start(self):
		if status == STATUS_WAITING:
			status = STATUS_STARTED
			return True
		return False

	def end(self):
		if status == STATUS_STARTED:
			status = STATUS_WAITING
			return True
		return False

	def toListDict(self):
		result = {}
		result[RESULT_ROOMID] = self.roomid
		result[RESULT_TITLE] = self.title
		result[RESULT_MAX_NUMBER] = self.max_number
		result[RESULT_CURRENT_NUMBER] = len(self.members)+1
		result[RESULT_TYPES] = self.types
		result[RESULT_WAGER] = self.wager
		result[RESULT_STATUS] = self.status
		result[RESULT_NICKNAME] = self.creator.nickname
		result[RESULT_USERID] = self.creator.user_id
		return result

	def toInfoDict(self):
		result = {}
		result[RESULT_TITLE] = self.title
		result[RESULT_MAX_NUMBER] = self.max_number
		result[RESULT_TYPES] = self.types
		result[RESULT_WAGER] = self.wager
		result[RESULT_STATUS] = self.status
		result[RESULT_NICKNAME] = self.creator.nickname
		result[RESULT_USERID] = self.creator.user_id
		result[RESULT_MEMBERS] = []
		for member in self.members:
			memberdict = {RESULT_NICKNAME:member.nickname,RESULT_USERID:member.user_id}
			result[RESULT_MEMBERS].append(memberdict)
		return result