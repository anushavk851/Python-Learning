#Print a hollow triangle
 #   *        
 #   *  *
 #   *     *
 #   * * * * *
 n=int(input("enter a number: "))
 for i in range(1,n+1):
    for j in range(1,i+1):
       if j==1 or i==n or i==j:
             print("*",end=" ")
       else:
          print(" ",end=" ")
    print()   
