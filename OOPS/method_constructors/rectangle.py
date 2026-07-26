#2 Rectangle
 # Create a Rectangle class.
 # Attributes: length, width
 # Methods:
  # area()
  # perimeter()
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def display(self):

        print("area is: ",self.length*self.width)
        print("perimeter is: ",2*(self.length+self.width))

r1=Rectangle(3,5)
r1.display()
r2=Rectangle(5,8)
r2.display()
