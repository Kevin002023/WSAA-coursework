import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "root",
  database= "wsaa"
)


cursor = db.cursor()

sql= "update student set age=%s where id = %s"

values = (19, 4) #comma is necessary as it only takes tuples

cursor.execute(sql, values)

db.commit()
print("1 record updated")

db.close()
cursor.close()