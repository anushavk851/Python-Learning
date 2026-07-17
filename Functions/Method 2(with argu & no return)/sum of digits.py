#Write a function that accepts a number and prints sum of its digit.
  def sum_digit(num):
      temp=num
      sum=0
      while temp>0:
          digit=temp%10
          sum=sum+digit
          temp=temp//10
      print("sum of digits of the number is : ",sum)

  n=int(input("enter a value: "))
  sum_digit(n)
