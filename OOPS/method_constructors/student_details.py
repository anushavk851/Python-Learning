#1 Student details
 # Create a Student class.
 # Attributes: name, age, mark
 # Constructor to initialize them.
 # Method to display student details.
class Student:
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark

    def display(self):
        print("student name: ",self.name)
        print("student age: ",self.age)
        print("student mark: ",self.mark)

s1=Student("anusha",25,80)
s1.display()
s2=Student("anusree",29,99)
s2.display()
s3=Student("bindu",26,88)
s3.display()
