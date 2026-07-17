#Find sum of odd numbers from 1 to n.
  n=int(input("enter a number: "))
  sum=0
  for i in range(0,n+1):
      if i%2!=0:
          sum=sum+i
  print("sum of odd numbers given is: ",sum)
