#Find the sum of even numbers from 1 to n.
n=int(input("enter a number: "))
i=2
sum=0
while i<=n:
  sum=sum+i
  i=i+2
print("sum of even numbers are: ",sum)
