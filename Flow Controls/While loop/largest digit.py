#Find the largest digit in a number.
n=int(input("enter a number: " ))
largest=0
while n>0:
  digits=n%10
  if digits>largest:
     largest=digits

  n= n//10
print("the largest digit is", largest)
