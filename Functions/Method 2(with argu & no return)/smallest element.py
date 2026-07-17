#Write a function that accepts a list and prints the Smallest element.
  def smallest(list1):
      smallest=list1[0]
      for i in list1:
          if i<smallest:
              smallest=i
      print("smallest number is: ",smallest)

  li=list(map(int,input().split()))
  smallest(li)
