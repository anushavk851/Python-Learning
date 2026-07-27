#10 Food Ordering System
 # Create food item objects
 # Display menu
 # Select items
 # Calculate total bill

class FoodItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_item(self):
        print(self.name, "-", self.price)

    def calculate_total(self, quantity):
        return self.price * quantity

food1 = FoodItem("Burger", 150)
food2 = FoodItem("Pizza", 250)
food3 = FoodItem("Fried Rice", 180)

print("MENU")
food1.display_item()
food2.display_item()
food3.display_item()

# Ordering
print("\n YOUR  ORDER ")

total = 0
quantity1 = int(input("Enter Burger quantity: "))
total = total + food1.calculate_total(quantity1)

quantity2 = int(input("Enter Pizza quantity: "))
total = total + food2.calculate_total(quantity2)

quantity3 = int(input("Enter Fried Rice quantity: "))
total = total + food3.calculate_total(quantity3)

print("\nTotal Bill:", total)
