#Mobile Class
 # Create a class named Mobile.
 # Attributes:
  # Brand
  # Model
 # Methods:
  # call()
  # message()
 # Sample Output:
 # Samsung is making a call.
 # Samsung sent a message.       
class Mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def call(self):
        print(f'{self.brand} is making a call')

    def message(self):
        print(f'{self.brand} sent a message')        

m1=Mobile("samsung","s24")
m1.call()
m1.message()
