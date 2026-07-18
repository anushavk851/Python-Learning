#Spy number-sum of digits=product of digits(eg 123: 1+2+3=6,1*2*3=6).
n=int(input("enter a number: "))
digits=[int(i) for i in str(n)]
s=sum(digits)
p=1
for i in digits:
    p=p*i
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
