#!/usr/bin/python3

import pymysql

dbserver = "localhost"
dbusername = "root"
dbpassword = "root"
dbname = "employee_logistics"


def login_check(username="",password=""):
	# Open database connection
	db = pymysql.connect(dbserver,dbusername,dbpassword,dbname)
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	# Prepare SQL query to INSERT a record into the database.
	sql = """SELECT username FROM admin WHERE username like '%s' and password like '%s'""" % (username,password)
	try:
		# Execute the SQL command
		cursor.execute(sql)
		# Fetch all the rows in a list of lists.
		results = cursor.fetchall()
		print(results)
		if len(results)==0:
			return False
		else:
			return True
	except:
		print ("Error: unable to fetch data")

	return False