#Write a function that accepts a string and return the reversed string.
  def reversed(string):
      rev=""
      for ch in string:
          rev=ch+rev
      return rev

  string1=input("enter a string: ")
  result=reversed(string1)
  print(result)
