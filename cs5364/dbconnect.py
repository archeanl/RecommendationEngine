import MySQLdb

def connection():
	conn =MySQLdb.connect(host="127.0.0.1",
					user="root",
					passwd="6264",
					db="DEVELOPMENT")
	c=conn.cursor()
	return c, conn
					
				
	

