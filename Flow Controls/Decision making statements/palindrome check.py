#Check whether a number is palindrome
  num=(input("enter a number: "))
  rev=num[::-1]
  if num==rev:
      print("its a palindrome")
  else:
      print("not a palindrome")
