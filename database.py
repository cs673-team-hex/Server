from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import util.user
import getpass

Base = declarative_base()

success = False
engine = None
session = None
while not success:
	try:
		#username = input("Enter username: ")
		#passwd = getpass.getpass("Enter password: ")
		engine = create_engine(\
			"mysql+mysqldb://%s:%s@localhost/virtual_vegas"%("root","hnxthwz2311245",))
		engine.connect()
		Session = sessionmaker(bind=engine)
		session = Session()
		success = True
	except Exception as e:
		print e;
		success = False

Base.metadata.create_all(engine) 

#ed_user = util.user.User(username='ed', nickname='Ed Jones', password='edspassword'\
#	,balance=12.34,credit=0,factor1=0,factor2=0,factor3=0)

#session.add(ed_user)
#session.commit()