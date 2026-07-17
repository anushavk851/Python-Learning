#Find the sum of odd numbers from 1 to n.
n=int(input("enter a value: "))
i=1
sum=0
while i<=n:
  sum=sum+i
  i=i+2
print("sum of odd numbers is: ",sum)
