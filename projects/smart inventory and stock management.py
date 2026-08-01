#SMART INVENTORY AND STOCK MANAGEMENT SYSTEM

# Features
    # Add products
    # View products
    # Search products
    # Update stock
    # Sell products
    # Automatically reduce stock
    # Low-stock report
    # Calculate inventory value
    # Sales history
    # Save data to files
    # File structure
    # inventory_project/

#program flow 

# ├── main.py
# ├── products.txt
# └── sales.txt


from datetime import datetime

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def display(self):
        print("\nProduct ID :", self.product_id)
        print("Name       :", self.name)
        print("Category   :", self.category)
        print("Price      :", self.price)
        print("Quantity   :", self.quantity)

    def inventory_value(self):
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self):
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        product = Product(
            product_id,
            name,
            category,
            price,
            quantity
        )

        self.products.append(product)
        self.save_products()

        print("Product added successfully.")

    def view_products(self):
        if len(self.products) == 0:
            print("No products available.")
            return

        for product in self.products:
            product.display()

    def search_product(self):
        keyword = input("Enter product name/category: ").lower()

        found = False

        for product in self.products:
            if (keyword in product.name.lower()
                    or keyword in product.category.lower()):

                product.display()
                found = True

        if not found:
            print("Product not found.")

    def update_stock(self):
        product_id = input("Enter product ID: ")

        for product in self.products:
            if product.product_id == product_id:

                print("Current stock:", product.quantity)

                amount = int(input("Enter stock to add: "))

                product.quantity += amount

                self.save_products()

                print("Stock updated.")
                return

        print("Product not found.")

    def sell_product(self):
        product_id = input("Enter product ID: ")

        for product in self.products:

            if product.product_id == product_id:

                amount = int(input("Enter quantity to sell: "))

                if amount <= product.quantity:

                    product.quantity -= amount

                    total = amount * product.price

                    self.save_products()
                    self.save_sale(product, amount, total)

                    print("Sale completed.")
                    print("Total amount:", total)

                else:
                    print("Insufficient stock.")

                return

        print("Product not found.")

    def low_stock(self):
        print("\nLOW STOCK PRODUCTS")

        found = False

        for product in self.products:

            if product.quantity <= 5:
                product.display()
                found = True

        if not found:
            print("No low-stock products.")

    def total_inventory_value(self):
        total = 0

        for product in self.products:
            total += product.inventory_value()

        print("Total inventory value:", total)

    def save_products(self):
        file = open("products.txt", "w")

        for product in self.products:
            data = (
                product.product_id + "|" +
                product.name + "|" +
                product.category + "|" +
                str(product.price) + "|" +
                str(product.quantity)
            )

            file.write(data + "\n")

        file.close()

    def load_products(self):
        file = open("products.txt", "a+")
        file.seek(0)

        for line in file:

            data = line.strip().split("|")

            if len(data) == 5:

                product = Product(
                    data[0],
                    data[1],
                    data[2],
                    float(data[3]),
                    int(data[4])
                )

                self.products.append(product)

        file.close()

    def save_sale(self, product, quantity, total):

        file = open("sales.txt", "a")

        date = datetime.now()

        record = (
            str(date) + " | " +
            product.name + " | " +
            str(quantity) + " | " +
            str(total)
        )

        file.write(record + "\n")

        file.close()

    def sales_history(self):

        file = open("sales.txt", "a+")
        file.seek(0)

        print("\nSALES HISTORY")

        content = file.read()

        if content == "":
            print("No sales available.")
        else:
            print(content)

        file.close()


def menu():

    inventory = Inventory()
    inventory.load_products()

    while True:

        print("\n========== INVENTORY SYSTEM ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Stock")
        print("5. Sell Product")
        print("6. Low Stock Products")
        print("7. Total Inventory Value")
        print("8. Sales History")
        print("9. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            inventory.add_product()

        elif choice == "2":
            inventory.view_products()

        elif choice == "3":
            inventory.search_product()

        elif choice == "4":
            inventory.update_stock()

        elif choice == "5":
            inventory.sell_product()

        elif choice == "6":
            inventory.low_stock()

        elif choice == "7":
            inventory.total_inventory_value()

        elif choice == "8":
            inventory.sales_history()

        elif choice == "9":
            print("Thank you.")
            break

        else:
            print("Invalid choice.")


menu()
