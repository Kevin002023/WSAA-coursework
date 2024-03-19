from studentDAO import studentDAO

student = {
  "name":"Janice",
  "age": 34
  }

#create
student = studentDAO.create(student)
studentId = student["id"]

#find by id
result = studentDAO.findById(studentId);
print("test create and find by id")
print(result)

#update
newstudentvalues = {"name":"fred", "age":15}
studentDAO.update(studentId,newstudentvalues)
result = studentDAO.findById(studentId);
print("test update")
print(result)

#get all
print("test get all")
allStudents = studentDAO.getAll() 
for student in allStudents:
  print(student)

#delete
studentDAO.delete(studentId)