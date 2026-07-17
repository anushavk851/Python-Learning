#Find the largest number until the user enters 0.
n=int(input("enter a value: "))
largest=0
while n!=0:
  if largest<n:
     largest=n
     n=int(input("enter another value: "))
  else:
     n=int(input("enter another value: "))
print("the largest of all is: "largest)
