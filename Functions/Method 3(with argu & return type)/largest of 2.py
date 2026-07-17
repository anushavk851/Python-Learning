#Write a function that accepts 2 numbers and return the larger number.
  def largest(n1,n2):
      if n1>n2:
          return n1
      elif n2>n1:
          return n2
      else:
          return "both are equal"

  n1=int(input("enter a number: "))
  n2=int(input("enter a number: "))
  larg=largest(n1,n2)
  print(larg)
