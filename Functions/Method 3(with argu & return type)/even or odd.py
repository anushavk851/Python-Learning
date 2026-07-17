#Write a function that accepts a number and return whether it is even or odd.
  def odd_even(n):
      if n%2==0:
          return "Even"
      else:
          return "Odd"

  n1=int(input("enter a value: "))
  result=odd_even(n1)
  print(result)
