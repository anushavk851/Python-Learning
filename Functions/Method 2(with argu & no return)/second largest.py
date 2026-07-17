#Write a function that accepts a list and prints the second largest element.
  def second_largest(list1):
      largest=list1[0]
      second=float('-inf')
      for i in list1:
          if i>largest:
              second=largest
              largest=i
          elif i>second and i!=largest:
              second=i
      print(second)

  li=list(map(int,input().split()))
  second_largest(li)
