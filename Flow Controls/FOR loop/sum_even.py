#Find the sum of even numbers from 1 to N.
  n=int(input("enter a number: "))
  sum=0
  for i in range(1,n+1):
      if i%2==0:
          sum=sum+i
  print("total sum of even numbers is: ",sum)
