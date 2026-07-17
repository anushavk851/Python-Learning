#Check whether a number is prime or not.
  n=int(input("enter a number: "))
  count=0
  for i in range(1,n+1):
      if n%i==0:
      count=count+1
  if count==2:
  print("its a prime number")
  else:
  print("not prime number") *)
