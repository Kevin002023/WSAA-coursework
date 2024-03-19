import mysql.connector

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