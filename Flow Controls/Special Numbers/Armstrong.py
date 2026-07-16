#Check whether a number is armstrong number.
  n=int(input("enter a number: "))
  temp=n
  sum=0
  count=len(str(n))
  for i in range(count):
      num=temp%10
      sum=sum+(num**count)
      temp=temp//10
  if sum==n:
      print("the given number is an amstrong")
  else:
      print("not an armstrong number")
