#Check whether a number is palindrome
  def palindrome():
      n=int(input("enter a number: "))
      temp=n
      rev=0
      while temp>0:
          digit=temp%10
          rev=rev*10+digit
          temp=temp//10
      if rev==n:
          print("number is palindrome")
      else:
          print("not palindrome")

  palindrome()
