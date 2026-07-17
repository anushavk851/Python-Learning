#Print even numbers from 1 to n.
  def even(n):
      if n==0:
          return 
      else:
          if n%2==0:
              print(n)
          even(n-1)
          
  num=int(input("enter a value: "))
  even(num)
