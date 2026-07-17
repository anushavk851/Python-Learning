#Write a function that accepts a number and return true if its prime otherwise false.
  def prime(n):
      count=0
      i=1
      for i in range(1,n+1):
          if n%i==0:
              count=count+1
          i=i+1
      if count==2:
          return "True"
      else:
          return "False"
      
  n1=int(input("enter a value: "))
  result=prime(n1)
  print(result)
