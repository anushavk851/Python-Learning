#Find the product of numbers from 1 to N.
  n=int(input("enter a value: "))
  fact=1
  for i in range(1,n+1):
      fact=fact*i
  print("factorial of the given number is : ",fact) 
