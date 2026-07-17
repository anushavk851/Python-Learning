#42 Find the first digit of a number
n=int(input("enter a number: "))
while n>=10:
  n=n//10
print("First digit of a number is: ",n)
