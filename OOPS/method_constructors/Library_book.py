#Library Book
 # Create a Book class with:
  # title
  # author
  # price
  # available
 # Methods:
  # display_book() → display all book details
  # borrow_book() → change availability to "Not Available"
  # return_book() → change availability back to "Available"

class Book:
  def __init__(self,title,author,price,available):
      self.title=title
      self.author=author
      self.price=price
      self.available=available

  def display_book(self):
      print(f' Title : {self.title} , author : {self.author}, price : {self.price}, availability: {self.available}')

  def borrow_book(self):
      if self.available=="available":
          self.available="Not available"
          print("Book Borrowed Successfully")
      else:
          print("Soryy,Book is Not Currently Available")

  def return_book(self):
      if self.available=="Not available":
          self.available="available"
          print("thank you for returning the book")
      else:
          print("Book is already available")
b1=Book("python programming","richard",1200,"available")
b1.borrow_book()
b1.display_book()
b1.return_book()
b1.display_book()
