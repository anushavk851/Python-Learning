#Write a Python program to accept a person's name, age, ticket type (Regular/Premium), and guardian availability (Yes/No).
 # If age is 18 or above:
 # If ticket type is Premium:
 # If the person has a valid ID, print "Premium Entry Allowed".
 # Otherwise, print "Premium Entry Denied".
 # Otherwise, print "Regular Entry Allowed".
 # If age is below 18:
 # If a guardian is available, print "Entry Allowed with Guardian".
 # Otherwise, print "Entry Denied".anu

  name=input("enter your name: ")
  age=int(input("enter your age: "))
  ticket=input("enter your ticket type (Regular/Premium) : ").lower()
  guardian_available=input("guardian availability(yes/no): ").lower()
  valid_id=input("do you have a valid id(yes/no): ").lower()
  if age >=18:
      if ticket =="premium":
          if valid_id=="yes":
              print("premium entry allowed")
          else:
              print("premium entry denied")
      else:
          print("regular entry allowed")
  else:
      if guardian_available=="yes":
          print("entry allowed with guardian")
      else:
          print("entry denied ")
