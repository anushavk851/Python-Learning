#Rotate digits once to right (12345-51234)
  n=int(input("enter a 4 digit number:" )) 
  last=n%10
  remaining= n//10
  result= (last*1000)+remaining
  print(result)
