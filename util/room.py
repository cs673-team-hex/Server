from random import shuffle
import constant
from util.deck import Deck
from blackjack.blackjackround import BlackJackRound

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

class Room:

	STATUS_WAITING = 1
	STATUS_STARTED = 2

	def __init__(self, roomid, title, max_number, types, creator, wager=10):
		self.roomid = roomid
		self.status = Room.STATUS_WAITING
		self.title = title
		self.max_number = max_number
		self.types = types
		self.wager = wager
		self.creator = creator
		self.members = {}
		self.round = None

	def addMember(self, member):
		if self.status != Room.STATUS_WAITING:
			return False
		if len(self.members)>=self.max_number-1:
			return False
		if member.user_id == self.creator.user_id:
			return False
		if member.user_id in self.members:
			return False
		self.members[member.user_id] = member
		return True

	def removeMember(self, memberid):
		if memberid == self.creator.user_id:
			del self.creator
			self.creator = None
			return True
		if memberid in self.members:
			del self.members[memberid]
			return True
		return False

	def start(self):
		if self.round is not None:
			self.round.clear()
			del self.round
		if self.status != Room.STATUS_WAITING:
			return False
		if self.types == constant.GAME_TYPE_BLACKJACK:
			playerArray = []
			playerArray.append(self.creator)
			for userid, member in self.members.items():
				playerArray.append(member)
			shuffle(playerArray)
			i = 1
			for player in playerArray:
				player.create(position=i)
				i+=1
			self.round = BlackJackRound(playerArray, Deck(), self.end, wager=self.wager)
			self.status = Room.STATUS_STARTED
			return True
		return False

	def end(self):
		if self.status == Room.STATUS_STARTED:
			self.status = Room.STATUS_WAITING
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
		for userid, member in self.members.items():
			memberdict = {RESULT_NICKNAME:member.nickname,RESULT_USERID:member.user_id}
			result[RESULT_MEMBERS].append(memberdict)
		return result