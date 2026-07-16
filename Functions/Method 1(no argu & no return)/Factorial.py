#Find the factorial of a number
  def factorial():
      num=int(input("enter a number: "))
      fact=1
      for i in range(1,num+1):
          fact=fact*i
      print(fact)

  factorial()
