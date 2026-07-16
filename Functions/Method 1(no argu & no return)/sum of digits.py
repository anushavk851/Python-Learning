#Find the sum of digits of a number.
  def add():
      n=int(input("enter a number: "))
      temp=n
      sum=0
      while temp>0:
          digits=temp%10
          sum=sum+digits
          temp=temp//10
      print(sum)

  add()
