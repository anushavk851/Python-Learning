#Print multiplication table of a number.
n=int(input("enter a value: "))
i=1
while 0<n and i<=10:
     product=n*(i) 
     print(n,"*",i,"=",product)
     i=i+1
