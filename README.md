# This is the server for Black Jack game.

Set up
============

1. Install pyOpenSSL::

  $ pip install pyopenssl

  The pyopenssl is a common library for SSL functions.
  See https://github.com/pyca/pyopenssl for detailed introduction of pyopenssl
   
2. Install sqlalchemy::

  $ pip install SQLAlchemy

  The sqlalchemy is a common library to use ORM in python
  The SQL injection protection also be well implemented in this library
  See http://www.sqlalchemy.org/ for detailed introduction of sqlalchemy
  
3. Import mysql database from db file

  $ mysql -u root --password=password virtual_vegas < virtual_vegas.db

  The username must be "root"
  
Start server
============

Run command as follow:

  $ python server.py port password
  
  Define the port and database password you used in this server

Documentation
=============

