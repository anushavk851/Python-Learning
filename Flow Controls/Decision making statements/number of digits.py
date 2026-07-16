#Check number of digit in the user input number
  num=int(input("enter a number: "))
  if num<10:
      print("its a single digit number")
  elif num<100:
      print("its a double digit number")
  elif num<1000:
      print("its a triple digit number")
  else:
      print("the number have more than 3 digits")
