#Check BMI category (18.5-24.9 is normal),take users weight and height and calculate bmi,print whether it is normal,low or high
  weight=float(input("enter your weight: "))
  height=float(input("enter your height: "))
  bmi=(weight)/((height/100)**2)
  print("your BMI is: ",bmi)
  if 18.5<= bmi <= 24.9:
          print("your BMI is normal")
  elif bmi<18.5:
          print("your BMI is low")
  else:
          print("your BMI is high")
