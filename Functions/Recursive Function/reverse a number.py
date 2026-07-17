#Reverse a number
  def reverse(n,rev=0):
      if n==0:
          return rev
      else:
          return reverse(n//10,rev*10+n%10)

  num=int(input("enter a number: "))
  print(reverse(num))
