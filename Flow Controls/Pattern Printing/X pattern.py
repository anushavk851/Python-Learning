#15 Print a X pattern using *.
 # *   *
 #  * * 
 #   *  
 #  * * 
 # *   *
n=int(input("enter odd size: "))
for i in range(n):
    for j in range(n):
        if j==i or j==n-i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
