#Student Management
 # Create a Student class with the following:
  # Attributes: student_id, name, course, marks
 # Methods:
  # Display student details.
 # Check whether the student has passed (pass mark = 40)
class Student:
    def __init__(self,student_id,name,course,mark):
        self.student_id=student_id
        self.name=name
        self.course=course
        self.mark=mark
    def display_student(self):
          print(f' student id: {self.student_id}')
          print(f' name:{self.name}')
          print(f' course name : {self.course}')
          print(f' mark : {self.mark}')
          if self.mark>=40:
               print(f' {self.name} have passed')
          else:
                print(f' {self.name} have failed')

s1=Student(12,"anu","python",56)
s1.display_student()
# s2=Student(13,"karthik","python",39)
# s2.display_student()
