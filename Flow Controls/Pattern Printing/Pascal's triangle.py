#13 Print a pascals triangle
 #         1
 #       1   1
 #     1   2   1
 #   1   3   3   1
n=int(input("enter number of rows: "))
for i in range(n):
    num=1
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(num,end=" ")
        num=num*(i-j)//(j+1)
    print() 
