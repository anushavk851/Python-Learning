#Write a function that accepts a string as an argument and prints whether it is a palindrome
  def text(string):
          if string==string[::-1]:
              print("palindrome")
          else:
              print("Not palindrome")

  string1=input("enter a string: ")
  text(string1)
