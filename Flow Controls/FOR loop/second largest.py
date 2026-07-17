#Find second largest in a list
  list1=list(map(int, input().split()))
  largest=float('-inf')
  second=float('-inf')
  for num in list1:
      if num>largest:
          second=largest
          largest=num
      elif num>second:
          second=num
  print(second)
