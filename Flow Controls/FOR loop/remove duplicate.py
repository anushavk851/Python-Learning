#Remove duplicate element from list without using set method
  list1 = list(map(int, input().split()))
  result = []
  for i in list1:
      if i not in result:
          result.append(i)
  print(result)
