import mysql.connector

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