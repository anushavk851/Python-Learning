#Shopping Cart
 # Create a Product class with:
 # Attributes: productid, productname, price, quantity
 # Methods:
  # Calculate the total cost.
 # Apply a 10% discount if the total cost exceeds ₹5000.
 # Display the final bill.

class Product:
    def __init__(self,productid, productname, price, quantity):
        self.productid=productid
        self.productname=productname
        self.price=price
        self.quantity=quantity
    def total_cost(self):
        total=self.price*self.quantity
        if total>5000:
            discount=total*10/100
            total=total-discount
            print(f' Total cost is Rs {total} after a discount of Rs {discount}')
        else:
            print(f'Total cost is Rs {total}')

p1=Product(101,"phone",25000,2) 
p1.total_cost()              
