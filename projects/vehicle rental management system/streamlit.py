import streamlit as st
from vehicle_rental import RentalSystem, Car, Bike


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Vehicle Rental System",
    page_icon="🚗",
    layout="wide"
)


# --------------------------------------------------
# CREATE RENTAL SYSTEM
# --------------------------------------------------

system = RentalSystem()

# Load existing vehicles from vehicles.txt
try:
    system.load_vehicles()
except FileNotFoundError:
    # If vehicles.txt doesn't exist, create an empty file
    open("vehicles.txt", "w").close()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚗 Vehicle Rental System")
st.write("Manage cars, bikes, rentals and returns easily.")


# --------------------------------------------------
# SIDEBAR MENU
# --------------------------------------------------

st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Add Car",
        "Add Bike",
        "View Vehicles",
        "Search Vehicle",
        "Rent Vehicle",
        "Return Vehicle",
        "Available Vehicles",
        "Rental History"
    ]
)


# ==================================================
# 1. ADD CAR
# ==================================================

if option == "Add Car":

    st.header("🚗 Add Car")

    vehicle_id = st.text_input("Vehicle ID")
    brand = st.text_input("Brand")
    model = st.text_input("Model")

    rent = st.number_input(
        "Rent per day",
        min_value=0.0,
        step=100.0
    )

    seats = st.number_input(
        "Number of seats",
        min_value=1,
        step=1
    )

    if st.button("Add Car"):

        if vehicle_id == "" or brand == "" or model == "":
            st.error("Please fill all the fields.")

        else:

            duplicate = False

            for vehicle in system.vehicles:

                if vehicle.vehicle_id == vehicle_id:
                    duplicate = True
                    break

            if duplicate:

                st.error("Vehicle ID already exists.")

            else:

                car = Car(
                    vehicle_id,
                    brand,
                    model,
                    rent,
                    seats
                )

                system.vehicles.append(car)
                system.save_vehicles()

                st.success("Car added successfully! 🚗")


# ==================================================
# 2. ADD BIKE
# ==================================================

elif option == "Add Bike":

    st.header("🏍️ Add Bike")

    vehicle_id = st.text_input("Vehicle ID")
    brand = st.text_input("Brand")
    model = st.text_input("Model")

    rent = st.number_input(
        "Rent per day",
        min_value=0.0,
        step=100.0
    )

    engine = st.text_input("Engine Capacity")

    if st.button("Add Bike"):

        if vehicle_id == "" or brand == "" or model == "" or engine == "":
            st.error("Please fill all the fields.")

        else:

            duplicate = False

            for vehicle in system.vehicles:

                if vehicle.vehicle_id == vehicle_id:
                    duplicate = True
                    break

            if duplicate:

                st.error("Vehicle ID already exists.")

            else:

                bike = Bike(
                    vehicle_id,
                    brand,
                    model,
                    rent,
                    engine
                )

                system.vehicles.append(bike)
                system.save_vehicles()

                st.success("Bike added successfully! 🏍️")


# ==================================================
# 3. VIEW VEHICLES
# ==================================================

elif option == "View Vehicles":

    st.header("🚘 All Vehicles")

    if len(system.vehicles) == 0:

        st.info("No vehicles available.")

    else:

        for vehicle in system.vehicles:

            with st.container():

                st.subheader(
                    f"{vehicle.brand} {vehicle.model}"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.write("**Vehicle ID:**", vehicle.vehicle_id)
                    st.write("**Brand:**", vehicle.brand)
                    st.write("**Model:**", vehicle.model)

                with col2:
                    st.write("**Rent/day:** ₹", vehicle.rent)

                    if vehicle.available:
                        st.success("Available")
                    else:
                        st.error("Rented")

                with col3:

                    if vehicle.vehicle_type == "Car":
                        st.write("**Type:** Car")
                        st.write("**Seats:**", vehicle.seats)

                    else:
                        st.write("**Type:** Bike")
                        st.write("**Engine:**", vehicle.engine)

                st.divider()


# ==================================================
# 4. SEARCH VEHICLE
# ==================================================

elif option == "Search Vehicle":

    st.header("🔍 Search Vehicle")

    keyword = st.text_input(
        "Enter brand or model"
    )

    if st.button("Search"):

        if keyword == "":
            st.warning("Please enter a brand or model.")

        else:

            found = False

            for vehicle in system.vehicles:

                if (
                    keyword.lower() in vehicle.brand.lower()
                    or
                    keyword.lower() in vehicle.model.lower()
                ):

                    found = True

                    st.subheader(
                        f"{vehicle.brand} {vehicle.model}"
                    )

                    st.write(
                        "**Vehicle ID:**",
                        vehicle.vehicle_id
                    )

                    st.write(
                        "**Rent/day:** ₹",
                        vehicle.rent
                    )

                    if vehicle.available:
                        st.success("Available")
                    else:
                        st.error("Rented")

                    if vehicle.vehicle_type == "Car":

                        st.write(
                            "**Type:** Car"
                        )

                        st.write(
                            "**Seats:**",
                            vehicle.seats
                        )

                    else:

                        st.write(
                            "**Type:** Bike"
                        )

                        st.write(
                            "**Engine:**",
                            vehicle.engine
                        )

                    st.divider()

            if not found:
                st.warning("Vehicle not found.")


# ==================================================
# 5. RENT VEHICLE
# ==================================================

elif option == "Rent Vehicle":

    st.header("🔑 Rent Vehicle")

    available = []

    for vehicle in system.vehicles:

        if vehicle.available:
            available.append(vehicle)

    if len(available) == 0:

        st.warning("No vehicles available for rent.")

    else:

        vehicle_options = []

        for vehicle in available:

            vehicle_options.append(
                f"{vehicle.vehicle_id} - "
                f"{vehicle.brand} {vehicle.model}"
            )

        selected = st.selectbox(
            "Select Vehicle",
            vehicle_options
        )

        customer = st.text_input(
            "Customer Name"
        )

        days = st.number_input(
            "Number of Days",
            min_value=1,
            step=1
        )

        if st.button("Rent Vehicle"):

            selected_id = selected.split(" - ")[0]

            selected_vehicle = None

            for vehicle in system.vehicles:

                if vehicle.vehicle_id == selected_id:
                    selected_vehicle = vehicle
                    break

            if customer == "":

                st.error(
                    "Please enter customer name."
                )

            else:

                total = (
                    selected_vehicle.rent
                    * days
                )

                selected_vehicle.available = False

                system.save_vehicles()

                system.save_rental(
                    customer,
                    selected_vehicle,
                    days,
                    total
                )

                st.success(
                    "Rental successful! 🎉"
                )

                st.write(
                    "**Customer:**",
                    customer
                )

                st.write(
                    "**Vehicle:**",
                    selected_vehicle.model
                )

                st.write(
                    "**Days:**",
                    days
                )

                st.write(
                    "**Total Amount:** ₹",
                    total
                )


# ==================================================
# 6. RETURN VEHICLE
# ==================================================

elif option == "Return Vehicle":

    st.header("🔄 Return Vehicle")

    rented = []

    for vehicle in system.vehicles:

        if not vehicle.available:
            rented.append(vehicle)

    if len(rented) == 0:

        st.info("No vehicles are currently rented.")

    else:

        vehicle_options = []

        for vehicle in rented:

            vehicle_options.append(
                f"{vehicle.vehicle_id} - "
                f"{vehicle.brand} {vehicle.model}"
            )

        selected = st.selectbox(
            "Select Vehicle",
            vehicle_options
        )

        if st.button("Return Vehicle"):

            selected_id = selected.split(" - ")[0]

            for vehicle in system.vehicles:

                if vehicle.vehicle_id == selected_id:

                    vehicle.available = True

                    system.save_vehicles()

                    st.success(
                        "Vehicle returned successfully! ✅"
                    )

                    break


# ==================================================
# 7. AVAILABLE VEHICLES
# ==================================================

elif option == "Available Vehicles":

    st.header("✅ Available Vehicles")

    available = []

    for vehicle in system.vehicles:

        if vehicle.available:
            available.append(vehicle)

    if len(available) == 0:

        st.warning("No vehicles available.")

    else:

        for vehicle in available:

            st.subheader(
                f"{vehicle.brand} {vehicle.model}"
            )

            st.write(
                "**Vehicle ID:**",
                vehicle.vehicle_id
            )

            st.write(
                "**Rent/day:** ₹",
                vehicle.rent
            )

            if vehicle.vehicle_type == "Car":

                st.write(
                    "**Type:** Car"
                )

                st.write(
                    "**Seats:**",
                    vehicle.seats
                )

            else:

                st.write(
                    "**Type:** Bike"
                )

                st.write(
                    "**Engine:**",
                    vehicle.engine
                )

            st.divider()


# ==================================================
# 8. RENTAL HISTORY
# ==================================================

elif option == "Rental History":

    st.header("📋 Rental History")

    try:

        with open("rentals.txt", "r") as file:

            content = file.read()

        if content == "":

            st.info("No rental history.")

        else:

            st.text(content)

    except FileNotFoundError:

        st.info("No rental history found.")
