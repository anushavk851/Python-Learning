class Movie:
    def __init__(self, name, price, available_seats):
        self.name = name
        self.price = price
        self.available_seats = available_seats

    def display(self):
        print("Movie:", self.name)
        print("Ticket Price:", self.price)
        print("Available Seats:", self.available_seats)

    def book_ticket(self, seats):
        if seats <= self.available_seats:
            self.available_seats -= seats
            print("\nTicket booked successfully")
            print("Total amount:", seats * self.price)
        else:
            print("\nNot enough seats available")


movie1 = Movie("Harry Potter", 200, 20)

movie1.display()
movie1.book_ticket(3)
movie1.book_ticket(21)
