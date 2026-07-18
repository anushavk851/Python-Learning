#Print a hollow pyramid.
 #     *
 #    * *
 #   *   *
 #  *     *
 # * * * * * 
n=int(input("enter number of rows: "))
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        if i==n-1:
            if j%2==0:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        else:
            if j==0 or j==2*i:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
