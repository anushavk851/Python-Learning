#Write a function that accepts a number and return its factorial.
  def factorial(n):
      fact=1
      i=1
      while i<=n:
          fact=fact*i
          i=i+1
      return fact

  n1=int(input("enter a value: "))
  result=factorial(n1)
  print(result)
