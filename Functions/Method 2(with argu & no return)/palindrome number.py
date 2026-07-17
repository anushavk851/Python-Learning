#Write a function that accepts a number and prints whether its an palindrome number.
  def palindrome(num):
      temp=num
      rev=0
      while temp>0:
          digit=temp%10
          rev=rev*10+digit
          temp=temp//10
      if rev==num:
          print("Palindrome")
      else:
          print("Not palindrome")

  n=int(input("enter a number: "))
  palindrome(n)
