import mysql.connector

#creating database

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "root"
)

# wouldnt work originally. 'caching_sha2_password'  wasnt supported. had to update mysql-connector and python

cursor = db.cursor()
cursor.execute("create database WSAA")

db.close()
cursor.close()


#Creating table

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "root",
  database= "wsaa"
)

cursor = db.cursor()
sql= "create table student (id INT AUTO_INCREMENT PRIMARY KEY, name varchar(250), age int(3))"

cursor.execute(sql)

db.close()
cursor.close()

#Insert Data

cursor = db.cursor()
sql= "insert into student (name, age) values(%s,%s)"
values = ("trevor",43)

cursor.execute(sql, values)

db.commit()
print("1 record inserted, ID:", cursor.lastrowid)

db.close()
cursor.close()

#View Data


sql= "select * from student where id = %s"

values = (4,) #comma is necessary as it only takes tuples

cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)

db.close()
cursor.close()

#Update Data

sql= "update student set age=%s where id = %s"
values = (19, 4) #comma is necessary as it only takes tuples

cursor.execute(sql, values)

db.commit()
print("1 record updated")

db.close()
cursor.close()

#Delete

sql= "delete from student where id = %s"
values = (5,) #comma is necessary as it only takes tuples
cursor.execute(sql, values)

db.commit()
print(f"1 record with Id {values} deleted")

db.close()
cursor.close()