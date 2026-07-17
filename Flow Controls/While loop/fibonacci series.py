#Print fibonacci series (0 1 1 2 3 5 8 13...)
n=int(input("enter a number: "))
n1=0
n2=1
i=0
while i<n:
  print(n1,end=" ")
  n3=n1+n2
  n1=n2
  n2=n3
  i=i+1
