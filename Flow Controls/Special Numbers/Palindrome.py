#Check whether a number is palindrome number.
  n=int(input("enter a number: "))
  temp=n
  count=0
  reverse=0
  for i in str(n):
      count=count+1
  for i in range(count):
      num=temp%10
      reverse=(reverse*10)+num
      temp=temp//10
  if n==reverse:
      print("the given number is palindrome")
  else:
      print("its not a palindrome number")
