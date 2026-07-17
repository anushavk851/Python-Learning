#write a function that accepts a list of numbers and return the maximum element.
  def maximum(list1):
      max=list1[0]
      for i in list1:
          if i>max:
              max=i
      return max

  li=list(map(int,input().split()))
  result=maximum(li)
  print(result)
