#Accept the number of unit consumed and calculate the electricity bill
 #first 100 unit-5$/unit
 #less than 200-7 /unit
 #above 200-10/unit
  unit=float(input("enter the consumed unit: "))
  if unit<=100:
      amount=unit*5
      print("total bill is :",amount)
  elif unit <=200:
      amount= (100*5)+(unit-100)*7
      print("total bill is : ",amount)
  elseif unit>200:
      amount=(100*5)+(100*7)+(unit-200)*10
      print("total bill is: ",amount)
  else:
        print("invalid")
