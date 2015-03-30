import json, log, constant
from operations import *

PARAMETER_RESULT = 'result'
PARAMETER_STATUS = 'status'
PARAMETER_ID = 'userid'
PARAMETER_OPERATION = 'opt'
PARAMETER_INFORMATION = 'info'

operations={'login':login,'signup':signup,'recharge':recharge,'tranhistory':tranhistory,\
'recordhistory':recordhistory,'createroom':createroom,'roomlist':roomlist,'quitroom':quitroom}

def handle_data(data_str, connectionuid):
	response = {PARAMETER_STATUS:constant.STATUS_SUCCESS,PARAMETER_RESULT:{}}
	data =None
	try:
		data = json.loads(data_str)
	except 	ValueError:
		response[PARAMETER_STATUS]=constant.STATUS_JSON_UNMATCHED
		log.warning('handler: receive none json data.'+data_str)
	if data is not None:
		opt = data[PARAMETER_OPERATION]
		requestuid = data[PARAMETER_ID]
		if opt is 'login':
			status,result,connectionuid = login(data_str)
		elif opt in operations:
			if connectionuid==requestuid:
				status,result = operations[opt](data[PARAMETER_INFORMATION])
				response[PARAMETER_STATUS] = status
				response[PARAMETER_RESULT] = result
				response[PARAMETER_ID] = connectionuid
			else:
				response[PARAMETER_STATUS]=constant.STATUS_INFORMATION_INVALID
				log.warning('handler: receive unmatched user id. Connection:'+connectionuid+'; Request:'+requestuid)				
		else:
			response[PARAMETER_STATUS]=constant.STATUS_OPERATION_UNSUPPORTED
			log.warning('handler: receive unsupported request. opt = '+opt)
	return json.dumps(response),connectionuid

#print handle_data('{"opt":"signup","info":{"passwd":"0A987B5CD87B5BBC","username":"hwz2","nickname":"Bob"}}')
#print handle_data('{"opt":"login","info":{"passwd":"0A987B5CD87B5BBC","username":"hwz2"}}')
#print handle_data('{"opt":"tranhistory","info":{"userid":"0000000001","page":1,"num":10}}')
#print handle_data('{"opt":"recordhistory","info":{"userid":"0000000001","page":1,"num":10}}')
#print handle_data('{"opt":"recharge","info":{"userid":1,"number":"0123456789012345","expire":"0718","securitynumber":"000","amount":12.34}}')
#print handle_data('{"opt":"tranhistory","info":{"page":1,"num":10,"userid":1}}')
#print handle_data('{"opt":"recordhistory","info":{"page":1,"num":10,"userid":1}}')
#print handle_data('{"opt":"createroom","userid":1,"info":{"title":"blackjackgame","number":8,"type":1,"wager":10,"userid":1}}',1)
#print handle_data('{"opt":"createroom","userid":2,"info":{"title":"blackjackgame","number":8,"type":1,"wager":10,"userid":2}}',2)
#print handle_data('{"opt":"createroom","userid":3,"info":{"title":"blackjackgame","number":8,"type":1,"wager":10,"userid":3}}',3)
#print handle_data('{"opt":"roomlist","userid":1,"info":{"page":1,"num":10, "type":1}}',1)
#print handle_data('{"opt":"quitroom","userid":1,"info":{"roomid":100000,"userid":1}}',1)
#print handle_data('{"opt":"roomlist","userid":1,"info":{"page":1,"num":10, "type":1}}',1)
