#Find the average of numbers from 1 to n.
n=int(input("enter a number: "))
i=1
sum=0
while i<=n:
  sum=sum+i
  i=i+1
print("average of the given numbers is: ",sum/n)
