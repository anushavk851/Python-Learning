#Sum of digits.
  def digits_sum(n):
      if n==0:
          return 0
      else:
          return n%10+digits_sum(n//10)

  num=int(input("enter a value: "))
  print(digits_sum(num))
