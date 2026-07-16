#Print a character triangle 
 #A 
 #A B 
 #A B C 
 #A B C D 
 #A B C D E 
 character="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 n=int(input(" enter the number of rows: "))
 for i in range(n):
    for j in range(i+1):
       print(character[j],end=" ")
    print()
