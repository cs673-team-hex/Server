import logging,datetime
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

def getTime():
	return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S\t')
def debug(data):
	logging.debug(getTime()+data);
def info(data):
	logging.info(getTime()+data);
def warning(data):
	logging.warning(getTime()+data);
def error(data):
	logging.error(getTime()+data);
def critical(data):
	logging.critical(getTime()+data);
