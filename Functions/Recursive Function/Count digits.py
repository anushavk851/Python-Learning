#Count digits
  def count_digits(n):
      if n==0:
          return 0 
      else:
          return 1+count_digits(n//10)

  digits=int(input("enter a value: "))
  print(count_digits(digits))
