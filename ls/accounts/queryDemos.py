#***(1) Returns all students from students table
## students = Student.objects.all()

#***(2) Returns first student from students table
## firststudent = Student.objects.first()

#***(3) Returns last student from students table
## laststudent = Student.objects.last()

#***(4) Returns single student by name
## studentbyname = Student.objects.get(name='Baftjar Jusufi')

#***(5) Returns single student by name
## studentbyname = Student.objects.get(id=4)

#***(6) Returns all teachers from teachers table
## teachers = Teacher.objects.all()

#***(7) Returns first student from students table
## firstteacher = Teacher.objects.first()

#***(8) Returns last student from students table
## lastteacher = Teacher.objects.last()

#***(9) Returns single student by name
## teacherbyname = Teacher.objects.get(name='Baftjar Jusufi')

#***(10) Returns single student by name
## teacherbyname = Teacher.objects.get(id=4)

#***(11) Returns all courses related to the student (firstStudent variable set above)
## firststudent.order_set.all()

#***(12) Returns all courses related to the teacher (firstteacher variable set above)
## firstteacher.order_set.all()


