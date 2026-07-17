#Print hello n times using recursive function.
  def text(n):
      if n==0:
          return 
      else:
          print("hello")
          text(n-1)

  num=int(input("enter a value: "))
  text(num)
