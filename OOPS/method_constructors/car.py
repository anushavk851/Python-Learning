#4 Car
 # Create a Car class.
 # Attributes: brand, model, price
 # Methods:
  # display_details()
  # discounted_price()
class Car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("brand: ",self.brand)
        print("model: ",self.model)
        print("price: ",self.price)
        print("discounted price: ",self.price-(self.price*10/100))

c1=Car("tata mootors","Nexon",850000)
c1.display()
