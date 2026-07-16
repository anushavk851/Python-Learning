#Find second largest number from 3 numbers
  n1=int(input("enter a number: "))
  n2=int(input("enter a number: "))
  n3=int(input("enter a number: "))
  if(n1>n2 and n1<n3) or (n1>n3 and n1<n2):
      print("second largest number is: ",n1)
  elif (n2>n1 and n2<n3) or (n2>n3 and n2<n1):
      print("second largest number is: ",n2)
  elif (n3>n1 and n3<n2) or (n3>n2 and n3<n1):
      print("second largest number is: ",n3)
  else:
      print("two or more numbers are equal so there is no second largest number")
