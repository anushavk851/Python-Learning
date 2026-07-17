#Write a function that accepts a string and print whether it contain only digit.
  def only_digit(string):
      if string.isdigit():
          print("it contain only digits")
      else:
          print("does not contain only digit")

  s=input("enter a string")
  only_digit(s)
