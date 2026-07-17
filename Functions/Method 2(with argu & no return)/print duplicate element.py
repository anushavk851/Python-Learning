#20 Write a function that accepts a list and prints the duplicate element.
  def duplicate(list1):
      for i in range(len(list1)):
          count=0
          for j in range(len(list1)):
              if list1[i]==list1[j]:
                  count=count+1
          if count>1 and list1[i] not in list1[0:i]:
              print(list1[i])
              
  li=list(map(int,input().split()))
  duplicate(li)
