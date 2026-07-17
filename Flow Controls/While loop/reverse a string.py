#Reverse a String using while loop.
string=input("enter a string: ")
i=len(string)-1
rev=""
while 0<=i:
  rev=rev+string[i]
  i=i-1
print("reversed string= ",rev)
