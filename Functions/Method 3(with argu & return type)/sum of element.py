#write a function that accepts a list of numbers and return the sum of all element.
  def sum_list(list1):
      sum=0
      for i in list1:
          sum=sum+i
      return sum

  li=list(map(int,input().split()))
  result=sum_list(li)
  print(result)
