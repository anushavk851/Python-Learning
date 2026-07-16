#23 Print charater pattern in alphabetic order
 #A 
 #B C 
 #D E F 
 #G H I J 
 n=int(input("enter a number: "))
 character="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 chara=0
 for i in range(1,n+1):
       for j in range(i):
          print(character[chara],end=" ")
          chara=chara+1
       print()
