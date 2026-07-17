#Write a function that accepts three numbers and returns the largest among them.
  def largest(n1,n2,n3):
      if n1>=n2 and n1>=n3:
              return n1
      elif n2>=n1 and n2>=n3:
              return n2
      else:
          return n3  

  n1=int(input("enter a number: "))
  n2=int(input("enter a number: "))
  n3=int(input("enter a number: "))
  result=largest(n1,n2,n3)
  print(result)
