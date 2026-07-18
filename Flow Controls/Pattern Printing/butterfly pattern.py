#Print a butterfly pattern
 # *     * 
 # * * * * 
 # * * * * 
 # *     * 
n=int(input("Enter size: "))
#upper half
for i in range(1,n+1):
    print("* " * i,end="")
    print("  " * (2* (n-i)),end="")
    print("* " * i)
#lower half
for i in range(n,0,-1):
    print("* " * i,end="")
    print("  " * (2*(n-i)),end="")
    print("* " * i)
