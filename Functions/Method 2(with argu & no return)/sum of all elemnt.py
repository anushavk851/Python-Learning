#Write a function that accepts a list and prints the sum of all element.
  def all_sum(list1):
      sum=0
      for i in list1:
          sum=sum+i
      print("sum of all element: ",sum)

  li=list(map(int,input().split()))
  all_sum(li)
