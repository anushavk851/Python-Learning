#2 Sum of first n natural numbers
  def sum(n):
      if n==1:
          return 1
      else:
         return n+sum(n-1)

  num=int(input("enter a value: "))
  print(sum(num))
