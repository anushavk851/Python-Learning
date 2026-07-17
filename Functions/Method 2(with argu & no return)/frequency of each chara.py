#Write a function that accepts a string and print the frequency of each character in a dict.
  def frequency_string(string):
      frequency={}
      for ch in string:
          if ch!=" ":
              if ch in frequency:
                  frequency[ch]=frequency[ch]+1
              else:
                  frequency[ch]=1
      print(frequency)

  s=input("enter a string: ")
  frequency_string(s)
