#Write a function that accepts a list of integers and returns the sum of all even numbers.
  def add(list1):
      sum=0
      for i in list1:
          if i%2==0:
              sum=sum+i
      return sum
  li=list(map(int,input().split()))
  result=add(li)
  print(result)
