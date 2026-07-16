#If name is less than 3 characters long display validation error "name must be atlest 3 characters" otherwise if its more than 30
  #character long display "name can have maximum 30 characters" otherwise print "name looks good"
  name=input("enter your name: ")
  lenght=len(name)
  if lenght<3:
  print("name must be atlest 3 characters")
  elif lenght>30 :
  print("name can have maximum 30 characters")
  else:
  print("name looks good")
