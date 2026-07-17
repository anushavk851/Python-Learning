#Find the smallest number until 0 is entered.
n=int(input("enter a value: "))
smallest=n
while n!=0:
  if smallest>n:
     smallest=n
     n=int(input("enter another values: "))
  else:
     n=int(input("enter another value: "))
print("smallest number out of all is : ",smallest)
