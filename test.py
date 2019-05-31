'''import mysql.connector as mc
try:

	mydb=mc.connect(
		host="localhost",
		user="root",
		passwd="",
		database="mygst"
	)

	mycursor=mydb.cursor();

	mycursor.execute("select * from users");

	result=mycursor.fetchall();

	for x in result:
		print(x)

except:
	print("error");
print(mydb)
'''
print("hello");
