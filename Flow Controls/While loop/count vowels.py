#Count the vowels in a string using while loop
string=input("enter a string: ").lower()
count=0
i=0
vowels=["a","e","i","o","u"]
while i<len(string):
  if string[i] in vowels:
     count=count+1
  i=i+1
print(count)   
