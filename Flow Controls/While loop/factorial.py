#33 Factorials of a number
n=int(input("enter a number: "))
fact=1
i=1
while i<=n:
  fact=fact*i
  i=i+1
print("factorial of given number is : ",fact)
