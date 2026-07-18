#Harshad(Niven) number-eg 18(18 is divisible by 9 which is (1+8)).
n=int(input("enter a number: "))
digit_sum=sum(int(i) for i in str(n))
if n%digit_sum==0:
    print("Harshad number")
else:
    print("Not Harshad number")
