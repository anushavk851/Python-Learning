#Check whether the number id armstrong number
n=int(input("enter a number: "))
temp=n
no_digit=len(str(n))
rev=0

while n>0:
  num=n%10
  rev=rev+num**no_digit
  n=n//10
if temp==rev:
  print("given number is armstrong")
else:
  print("it's not armstrong")
