#write a function that accepts a string and return True if it is palindrome ,otherwise False
  def palindrome(string):
      rev=""
      for ch in string:
          rev=ch+rev
      if rev==string:
          return True
      else:
          return False

  string1=input("enter a string: ")
  result=palindrome(string1)
  print(result)
