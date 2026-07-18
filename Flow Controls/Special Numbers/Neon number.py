#Neon numbers-eg 9(9^2=81,8+1=9).
n=int(input("enter a number: "))
square=n*n
digit_sum=sum(int(i) for i in str(square))
if digit_sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
