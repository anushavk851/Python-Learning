#Print multiplication table for a number taken from user.
  num=int(input("enter a number: "))
  for i in range(1,11):
      print(f"{i} X {num} = {num*i}")
