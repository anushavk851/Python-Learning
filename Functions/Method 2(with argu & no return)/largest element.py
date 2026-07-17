#Write a function that accepts a list and prints the largest element.
  def largest(list1):
      largest=list1[0]
      for i in list1:
          if i>largest:
              largest=i
      print(largest)

  li=list(map(int,input().split()))
  largest(li)
