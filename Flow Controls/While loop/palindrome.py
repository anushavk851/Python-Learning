#Check whether a number is palindrome
n=int(input("enter a number: "))
temp=n
rev=0
while n>0:
  number=n%10
  rev=(rev*10)+number
  n=n//10
  
if rev==temp:
  print("it is a palindrome")
else:
  print("not palindrome")
