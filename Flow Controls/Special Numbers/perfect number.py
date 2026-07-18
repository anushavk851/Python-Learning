#Perfect number-eg 28(sum of proper divisor=num)
n=int(input("enter a number: "))
total=0

for i in range(1,n):
    if n%i==0:
        total=total+1
if total==n:
    print("perfect")
else:
    print("Not Perfect number")
