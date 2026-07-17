#Print numbers from 1 to n
  def numbers(n):
      if n==0:
          return 
      else:
          numbers(n-1)
          print(n)
  num=int(input("enter a value: "))
  numbers(num)
