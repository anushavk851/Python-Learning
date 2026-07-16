#Find the largest of 3 numbers
  num1=int(input("Enter a number: "))
  num2=int(input("Enter a number: "))
  num3=int(input("Enter a number: "))
  if num1>num2 and num1>num3:
          print("first number is the largest")
  elif num2>num3 and num2>num1:
      print("second number is largest")
  else:
      print("third number is largest")
