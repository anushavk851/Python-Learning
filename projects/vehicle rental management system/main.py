# VEHICLE RENTAL Features
    # 1. Add Car
    # 2. Add Bike
    # 3. View Vehicles
    # 4. Search Vehicle
    # 5. Rent Vehicle
    # 6. Return Vehicle
    # 7. Available Vehicles
    # 8. Rental History
    # 9. Exit

from datetime import datetime

class Vehicle:
    def __init__(self, vehicle_id, brand, model, rent):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent = rent
        self.available = True

    def display(self):
        print("\nID     :", self.vehicle_id)
        print("Brand    :", self.brand)
        print("Model    :", self.model)
        print("Rent/day :", self.rent)
        if self.available:
            print("Status   :", "Available")
        else:
            print("Status   :", "Rented")

class Car(Vehicle):

    def __init__(self, vehicle_id, brand, model, rent, seats):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent = rent
        self.available = True
        self.seats = seats
        self.vehicle_type = "Car"

    def display(self):
        print("\nID       :", self.vehicle_id)
        print("Brand    :", self.brand)
        print("Model    :", self.model)
        print("Rent/day :", self.rent)
        if self.available:
            print("Status   : Available")
        else:
            print("Status   : Rented")
        print("Seats    :", self.seats)
class Bike(Vehicle):

    def __init__(self, vehicle_id, brand, model, rent, engine):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent = rent
        self.available = True
        self.engine = engine
        self.vehicle_type = "Bike"

    def display(self):
        print("\nID       :", self.vehicle_id)
        print("Brand    :", self.brand)
        print("Model    :", self.model)
        print("Rent/day :", self.rent)
        if self.available:
            print("Status   : Available")
        else:
            print("Status   : Rented")
        print("Engine   :", self.engine)

class RentalSystem:

    def __init__(self):
        self.vehicles = []

    def add_car(self):

        vehicle_id = input("Enter car ID:")

        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
               print("Vehicle ID already exists.")
               return
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        rent = float(input("Enter rent per day: "))
        seats = int(input("Enter number of seats: "))
        car = Car(vehicle_id, brand, model, rent, seats)
        self.vehicles.append(car)
        self.save_vehicles()
        print("Car added.")

    def add_bike(self):

        vehicle_id = input("Enter Bike ID:")
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                print("Vehicle ID already exists.")
                return
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        rent = float(input("Enter rent per day: "))
        engine = input("Enter engine capacity: ")
        bike = Bike(vehicle_id,brand,model,rent,engine )
        self.vehicles.append(bike)
        self.save_vehicles()
        print("Bike added.")

    def view_vehicles(self):

        if len(self.vehicles) == 0:
            print("No vehicles available.")
            return
        for vehicle in self.vehicles:
            vehicle.display()

    def search_vehicle(self):

        keyword = input("Enter brand/model: ").lower()
        found = False
        for vehicle in self.vehicles:

            if (keyword in vehicle.brand.lower() or keyword in vehicle.model.lower()):
                vehicle.display()
                found = True
        if not found:
            print("Vehicle not found.")

    def rent_vehicle(self):
        vehicle_id = input("Enter vehicle ID: ")
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                if vehicle.available:

                    customer = input("Enter customer name: ")
                    days = int(input("Enter number of days: "))
                    if days <= 0:
                        print("Number of days must be greater than 0.")
                        return
                    total = vehicle.rent * days
                    vehicle.available = False
                    self.save_vehicles()
                    self.save_rental(customer,vehicle,days,total)

                    print("\nRental successful.")
                    print("Customer:", customer)
                    print("Vehicle :", vehicle.model)
                    print("Days    :", days)
                    print("Total   :", total)

                else:
                    print("Vehicle already rented.")

                return
        print("Vehicle not found.")

    def return_vehicle(self):

        vehicle_id = input("Enter vehicle ID: ")
        for vehicle in self.vehicles:

            if vehicle.vehicle_id == vehicle_id:

                if not vehicle.available:
                    vehicle.available = True
                    self.save_vehicles()
                    print("Vehicle returned successfully.")
                else:
                    print("Vehicle was not rented.")
                return
        print("Vehicle not found.")

    def available_vehicles(self):

        print("\nAVAILABLE VEHICLES")
        found = False

        for vehicle in self.vehicles:

           if vehicle.available:
              vehicle.display()
              found = True

        if not found:
            print("No vehicles available.")

    def save_vehicles(self):

        with open("vehicles.txt", "w") as file:

            for vehicle in self.vehicles:

                if vehicle.vehicle_type == "Car":
                    data = ("Car|" + vehicle.vehicle_id + "|" +vehicle.brand + "|" +vehicle.model + "|" +
                        str(vehicle.rent) + "|" +str(vehicle.seats) + "|" +str(vehicle.available))

                else:
                    data = ("Bike|" + vehicle.vehicle_id + "|" +vehicle.brand + "|" +vehicle.model + "|" +
                        str(vehicle.rent) + "|" +vehicle.engine + "|" +str(vehicle.available))

                file.write(data + "\n")

    def load_vehicles(self):

        with open("vehicles.txt", "r") as file:

         for line in file:

            data = line.strip().split("|")
            if len(data) == 7:

                if data[0] == "Car":
                    vehicle = Car(data[1],data[2],data[3],float(data[4]),int(data[5]))
                else:
                    vehicle = Bike(data[1],data[2],data[3],float(data[4]),data[5])

                vehicle.available = data[6] == "True"
                self.vehicles.append(vehicle)

    def save_rental(self,customer,vehicle,days,total):

        with open("rentals.txt", "a") as file:
            date = datetime.now()
            data = (str(date) + " | " +customer + " | " +vehicle.vehicle_id + " | " +vehicle.model + " | " +str(days) + " | " +str(total))
            file.write(data + "\n")

    def rental_history(self):

        with open("rentals.txt", "r") as file:

         content = file.read()

         print("\nRENTAL HISTORY")

         if content == "":
             print("No rental history.")
         else:
             print(content)

def menu():
    system = RentalSystem()
    system.load_vehicles()

    while True:

        print("\nVEHICLE RENTAL")
        print("1. Add Car")
        print("2. Add Bike")
        print("3. View Vehicles")
        print("4. Search Vehicle")
        print("5. Rent Vehicle")
        print("6. Return Vehicle")
        print("7. Available Vehicles")
        print("8. Rental History")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_car()
        elif choice == "2":
            system.add_bike()
        elif choice == "3":
            system.view_vehicles()
        elif choice == "4":
            system.search_vehicle()
        elif choice == "5":
            system.rent_vehicle()
        elif choice == "6":
            system.return_vehicle()
        elif choice == "7":
            system.available_vehicles()
        elif choice == "8":
            system.rental_history()
        elif choice == "9":
            break
        else:
            print("Invalid choice.")

#cd VehicleRental
#streamlit run app.py
