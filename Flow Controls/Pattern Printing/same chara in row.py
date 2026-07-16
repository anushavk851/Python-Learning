#22 Print character triangle with same character in row
 #A 
 #B B 
 #C C C 
 #D D D D 
 character="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 n=int(input(" enter the number of rows: "))
 for i in range(n):
    for j in range(i+1):
       print(character[i],end=" ")
    print()
