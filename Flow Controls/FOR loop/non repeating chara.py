#Find the first non repeating character in a string.
  s = input()
  for ch in s:
      if s.count(ch) == 1:
          print(ch)
          break
