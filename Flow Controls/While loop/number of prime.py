#Check whether a number is prime or not.
n=int(input("enter a number: "))
i=2
while i<n:
  if n%i==0:
     print("number is not prime")
     break
  i=i+1
else:
  if n>1:
  print("number is prime")
  else: 
     print("number is not prime")
