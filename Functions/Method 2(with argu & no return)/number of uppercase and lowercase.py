#Write a function that accepts a string and prints the number of uppercase and lowercase letters.
  def upper_lower(string):
      lower=0
      upper=0
      i=0
      while i<len(string):
          if string[i].isupper():
              upper=upper+1
          elif string[i].islower():
              lower=lower+1
          i=i+1
      print("Upper case: ",upper)
      print("Lower case: ",lower)
          
  string1=input("enter the string: ")
  upper_lower(string1)
