#Reverse a digits
  n=int(input("enter a number: "))
  count=0
  rev=0
  for i in str(n):
      count=count+1
  for i in range(count):
      num=n%10
      rev=rev*10+num
      n=n//10
  print("reversed digit is: ",rev)
