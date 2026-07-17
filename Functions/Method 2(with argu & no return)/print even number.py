#Write a function that accepts a list and prints only the even numbers.
  def even(list1):
      for i in list1:
          if i%2==0:
              print(i,end=" ")

  li=list(map(int,input().split()))
  even(li)
