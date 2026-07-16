#find the product of first and last digit number
  n=int(input("enter a 5 digit number: "))
  first= (n//10000)
  last= n%10
  print("product of first and last digit is : ",(first*last))
