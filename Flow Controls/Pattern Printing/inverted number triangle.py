#Print a inverted number triangle.
 #1 2 3 4
 #1 2 3
 #1 2 
 #1  
 n= int(input("enter the number of rows: "))
 for i in range(n,0,-1):
    for j in range(1,i+1):
       print(j,end=" ")
    print()
