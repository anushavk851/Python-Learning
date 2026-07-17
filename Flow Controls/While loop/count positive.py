#Count positive number until 0 is entered.
n=int(input("enter a number: "))
count=0
while n!=0:
  if n>0:
     count=count+1
     n=int(input("enter another value: "))
  else:
     n=int(input("enter another value: "))
print("count of positive number is : ",count)  
