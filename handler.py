import json, log, constant
from operations import *

PARAMETER_RESULT = 'result'
PARAMETER_STATUS = 'status'
PARAMETER_ID = 'userid'
PARAMETER_OPERATION = 'opt'
PARAMETER_INFORMATION = 'info'

operations={'login':login,'signup':signup,'purchase':purchase,'tranhistory':tranhistory,\
'recordhistory':recordhistory,'createroom':createroom,'roomlist':roomlist,'quitroom':quitroom,\
'gameresult':gameresult,'roominfo':roominfo,'joinroom':joinroom,'startgame':startgame,\
'blackjack':blackjackhandler,'blackjackroundinfo':blackjackroundinfo}

def handle_data(data_str, connectionuid):
	print data_str
	response = {PARAMETER_STATUS:constant.STATUS_SUCCESS,PARAMETER_ID:connectionuid,PARAMETER_RESULT:{}}
	data =None
	try:
		data = json.loads(data_str)
	except 	ValueError:
		response[PARAMETER_STATUS]=constant.STATUS_JSON_UNMATCHED
		log.warning('handler: receive none json data.'+data_str)
	if data is not None and PARAMETER_OPERATION in data and PARAMETER_ID in data:
		opt = data[PARAMETER_OPERATION]
		requestuid = data[PARAMETER_ID]
		if opt == 'login':
			status,result,connectionuid = login(data[PARAMETER_INFORMATION])
			response[PARAMETER_STATUS] = status
			response[PARAMETER_RESULT] = result
			response[PARAMETER_ID] = connectionuid
		elif opt in operations:
			if connectionuid==requestuid:
				data[PARAMETER_INFORMATION][PARAMETER_ID] = connectionuid
				status,result = operations[opt](data[PARAMETER_INFORMATION])
				response[PARAMETER_STATUS] = status
				if result!=None:
					response[PARAMETER_RESULT] = result
				response[PARAMETER_ID] = connectionuid
			else:
				response[PARAMETER_STATUS]=constant.STATUS_INFORMATION_INVALID
				log.warning('handler: receive unmatched user id. Connection:%d, Request:%d'%(connectionuid,requestuid))				
		else:
			response[PARAMETER_STATUS]=constant.STATUS_OPERATION_UNSUPPORTED
			log.warning('handler: receive unsupported request. opt = '+opt)
	else:
		log.warning('handler: missing parameter.')
		response[PARAMETER_STATUS] = constant.STATUS_PARAMETER_UNMATCHED
	print json.dumps(response)
	return json.dumps(response),connectionuid

#print handle_data('{"opt":"signup","info":{"passwd":"0A987B5CD87B5BBC","username":"hwz2","nickname":"Bob"}}')
#print handle_data('{"opt":"login","userid":0,"info":{"passwd":"0A987B5CD87B5BBC","username":"hwz2"}}',0)
#print handle_data('{"opt":"tranhistory","info":{"userid":"0000000001","page":1,"num":10}}')
#print handle_data('{"opt":"recordhistory","info":{"userid":"0000000001","page":1,"num":10}}')
#print handle_data('{"opt":"recharge","info":{"userid":1,"number":"0123456789012345","expire":"0718","securitynumber":"000","amount":12.34}}')
#print handle_data('{"opt":"tranhistory","info":{"page":1,"num":10,"userid":1}}')
#print handle_data('{"opt":"recordhistory","info":{"page":1,"num":10,"userid":1}}')
#print handle_data('{"opt":"createroom","userid":1,"info":{"title":"blackjackgame","number":8,"type":1,"wager":10,"userid":1}}',1)
#print handle_data('{"opt":"createroom","userid":2,"info":{"title":"blackjackgame","number":8,"type":1,"wager":10,"userid":2}}',2)
handle_data('{"opt":"createroom","userid":5,"info":{"wager":50,"number":8,"title":"Noob","type":1}}',5)
print handle_data('{"opt":"joinroom","userid":7,"info":{"roomid":100000}}',7)
handle_data('{"opt":"startgame","userid":5,"info":{"roomid":100000}}',5)
handle_data('{"opt":"blackjackroundinfo","userid":5,"info":{"roomid":100000}}',5)
import random
for i in range(1,5):
	operatiion = random.randint(1,4)
	handle_data('{"opt":"blackjack","userid":5,"info":{"roomid":100000,"opt":%d}}'%(1),5)
	handle_data('{"opt":"blackjackroundinfo","userid":5,"info":{"roomid":100000}}',5)
for i in range(1,5):
	operatiion = random.randint(1,4)
	print handle_data('{"opt":"blackjack","userid":7,"info":{"roomid":100000,"opt":%d}}'%(1),7)
	print handle_data('{"opt":"blackjackroundinfo","userid":7,"info":{"roomid":100000}}',7)
#print handle_data('{"opt":"roomlist","userid":1,"info":{"page":1,"num":10, "type":1}}',1)
#print handle_data('{"opt":"quitroom","userid":1,"info":{"roomid":100000,"userid":1}}',1)
#print handle_data('{"opt":"roomlist","userid":1,"info":{"page":1,"num":10, "type":1}}',1)
