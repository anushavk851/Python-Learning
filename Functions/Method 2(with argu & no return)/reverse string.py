#Write a function that accepts a string and prints the reverse of the string.
  def reversed(string):
      rev=" "
      for ch in string:
          rev=ch+rev
      print(rev)
  string1=input("enter a string: ")
  reversed(string1)   
