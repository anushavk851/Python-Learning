#Create a tuple of 6 numbers .
 #a use a 4 loop and print all elements 
 #b print even numbers present in it
    
  tup=(10,21,31,40,50,6)
  for i in tup:
      print(i)
    
  print("even numbers are:")  
  for i in tup:
      if i%2==0:
          print(i)
