#print fibonacci series
def fibonacci(n):                           
    if n==1 or n==0:
        return n  
    else:
        return  fibonacci(n-1)+fibonacci(n-2)  
    
num=int(input("enter a value: "))
for i in range(num):  
        print(fibonacci(i),end=" ")
