#10 function that takes a string as input and
 # returns a
 # dictionary containing the frequency(count) of each character in the string.
 # The characters
 # should be used as keys and their occurrence counts as values.
 # Ignore all space
 # characters while counting.
 # Example:
 # Input:
 # "hello world"
 # Output: {'h': 1,'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

  string=input()
  frequency={}
  for ch in string:
      if ch!=" ":
          if ch in frequency:
              frequency[ch]=frequency[ch]+1
          else:
              frequency[ch]=1

  print(frequency)
