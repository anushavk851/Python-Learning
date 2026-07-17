#Write a function that accepts a list of numbers and return product of digits.
  def product_digit(num):
      temp=num
      product=1
      while temp>0:
          digit=temp%10
          product=product*digit
          temp=temp//10
      return product

  n=int(input("ente the number: "))
  result=product_digit(n)
  print(result) 
