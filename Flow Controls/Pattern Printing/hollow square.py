#Print a hollow square
 #*  *  *  *    #i=0 all printed
 #*        *    #when j is 0 all printed.when j is n-1 all printed,
 #*        *    #j=0 or j==n-1 
 #*  *  *  *    #i=n-1 all printed

 n=int(input("enter a value: "))
 for i in range(n):
    for j in range(n):
       if i==0 or i==n-1 or j==0 or j==n-1:
          print("* ",end=" ")
       else:
             print("  ",end=" ")
    print()
