#Write a function that accepts a number and return sum of its digits.
  def sum_digit(num):
      temp=num
      sum=0
      while temp>0:
          digit=temp%10
          sum=sum+digit
          temp=temp//10
      return sum

  n=int(input("enter a value: "))
  result=sum_digit(n)
  print(result)
