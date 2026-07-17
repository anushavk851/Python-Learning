#Count uppercase and lowercase letters in a string using a while loop
string=input("enter a string: ")
upper=0
lower=0
i=0

while i<len(string):
  if string[i].isupper():
     upper=upper+1
  else:
     lower=lower+1
  i=i+1
print("number of uppercase present in given string is: ",upper)
print("number of lowercase present in given string is: ",lower)
