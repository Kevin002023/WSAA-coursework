import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password= "root",
  database= "wsaa"
)


cursor = db.cursor()

sql= "delete from student where id = %s"

values = (5,) #comma is necessary as it only takes tuples

cursor.execute(sql, values)

db.commit()
print(f"1 record with Id {values} deleted")

db.close()
cursor.close()