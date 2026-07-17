#Find the sum of digits of a number.
  n=int(input("enter a number: "))
  count=0
  sum=0
  for i in str(n):
      count=count+1
  for i in range(count):
      num=n%10
      sum=sum+num
      n=n//10
  print("sum of digits of the given number is: ",sum)
