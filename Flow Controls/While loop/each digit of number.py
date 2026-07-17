#Print each digit of a number on a new line.
n=int(input("enter a number: "))
temp=n
while temp>0:
  rev=temp%10
  temp=temp//10
while rev>0:
  print(rev%10)
  rev=rev//10
