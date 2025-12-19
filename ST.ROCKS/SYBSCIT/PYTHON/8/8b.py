
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	username="root",
	password="",
	database ="shekharsuman_db"
	)
# print(mydb)
mycursor = mydb.cursor()

mycursor.execute("drop table if exists students")
print("student table drop")

mycursor.execute("""create table students(id int auto_increment primary key, 
				name varchar(25), email varchar(25), age varchar(5), mobile varchar(10))""")
print("table created")
	
sql="insert into students(name, email, age, mobile) values(%s, %s, %s, %s)"
val=[
	('Shekhar Suman', 'shekharsuman@gmail.com', '19', '9304187853'),
	('Shreyansh Singh', 'shreyanshsingh@gmail.com', '22', '9367834932'),
	('Priti Chauhan', 'pritichauhan@gmail.com', '23', '879613522'),
	('Alister Qunney', 'alister@gmail.com', '24', '8796137857'),
	('Shraddha Patil','shraddhapatil@gmail.com','19','6202359556'),
	('Arvind Gupta', 'arvindgupta@gmail.com', '25', '9619024590'),
	('Pallavi Gupta', 'pallavigupta@gmail.com', '22', '9304125678'),
	('Hello Gupta', 'pallavigupta@gmail.com', '22', '9304125678')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "Record was inserted.")

print()

mycursor.execute("select * from students")
myresult = mycursor.fetchall()
# print(myresult)
for x in myresult:
	print(x)