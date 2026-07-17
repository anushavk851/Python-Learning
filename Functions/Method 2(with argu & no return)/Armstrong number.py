#Write a function that accepts a number and prints whether its an armstrong number.
    def armstrong(num):
        no_digit=len(str(num))
        temp=num
        sum=0
        while temp>0:
            digit=temp%10
            sum=sum+digit**no_digit
            temp=temp//10
        if sum==num:
            print("armstrong number")
        else:
            print("not armstrong")
            
    n=int(input("enter a value: "))
    armstrong(n)
