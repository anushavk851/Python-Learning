#Find the sum of multiples of 3 up to n.
n=int(input("enter a number: "))
i=3
sum=0
while i<=n:
  sum=sum+i
  i=i+3
print("sum of multiples of 3 up to", n, "is: ", sum)
