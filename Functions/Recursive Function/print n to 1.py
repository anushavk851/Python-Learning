#print from n to 1
  def number(n):
      if n==0:
          return 
      else:
          print(n)
          number(n-1)
      
  num=int(input("enter a value: "))
  number(num)
