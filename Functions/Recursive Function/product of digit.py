#Product of digits
  def product_digits(n):
      if n==0:
          return 1
      else:
          return(n%10)*product_digits(n//10)

  num=int(input("enter a number: "))
  print(product_digits(num))
