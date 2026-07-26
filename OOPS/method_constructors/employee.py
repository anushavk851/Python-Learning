#3 Employee
 # Create an Employee class.
 # Attributes: name, id, salary
 # Method to display employee details.
 # Create 3 employee objects.
class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def display(self):
        print("name of employee: ",self.name)
        print("id of employee: ",self.id)
        print("salary of employee: ",self.salary)

s1=Employee("anusha",101,25000)
s1.display()
s2=Employee("anusree",102,60000)
s2.display()
s3=Employee("keerthi",103,45000)
s3.display()
