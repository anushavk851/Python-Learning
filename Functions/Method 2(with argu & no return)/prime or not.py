#Write a function that accepts a number and print whether it is prime or not
  def prime(num):
      count=0
      for i in range(1,n+1):
          if num%i==0:
              count=count+1
      if count==2:
              print("its prime")
      else:
          print("not prime")

  n=int(input("enter a value: "))
  prime(n)
