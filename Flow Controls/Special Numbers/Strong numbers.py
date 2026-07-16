#3 Strong number
  n=int(input("enter a number: "))
  temp=n
  sum=0
  while temp>0:
      digit=temp%10
      fact=1
      for i in range(1,digit+1):
          fact=fact*i
      sum=sum+fact
      temp=temp//10
  if sum==n:
      print(n, "is a strong number")
  else:
      print(n, "is not a strong number")

