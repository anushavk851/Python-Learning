#Find smallest digit in a number
n=int(input("enter a number: "))
smallest=9
while n>0:
  digits=n%10
  if digits<smallest:
     smallest=digits

  n=n//10
print("smallest digit is: ",smallest)  
