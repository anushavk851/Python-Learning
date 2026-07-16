#Classify a person based on age(child,teenager,adult and senior citizen)
  age=int(input("enter your age: "))
  if age<13:
      print("you are a child")
  elif age<20:
      print("you are a teenager")
  elif age<60:
      print("you are an adult")
  else:
      print("you are a senior citizen")
