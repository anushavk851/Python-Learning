#Create a Simple calculator
  num1=int(input("enter a number: "))
  num2=int(input("enter a number: "))
  operator=input("enter any operator(+,-,*,/): ")
  if operator == "+" :
          num=num1+num2
          print("result is:",num)  
  elif operator == "-":
          num=num1-num2
          print("result is:",num)
  elif operator == "*":
          num=num1*num2
          print("result is:",num)
  elif operator == "/":
          num=num1/num2
          print("result is:",num)
  else:
          print("invalid operator")
