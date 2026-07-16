#20 Check whether a person is eligible for blood donation(age btw 18 and 65,weight min 50)
  age=int(input("enter your age: "))
  weight=int(input("enter your weight: "))
  if 18<= age <= 65 and weight>=50:
      print("you are eligible for donation")
  else:
      print("you are not eligible")
