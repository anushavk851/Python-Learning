#Write a function that accepts a string and return the number of vowels in it.
  def vowel_count(string):
      count=0
      for ch in string:
          if ch in "aeiouAEIOU":
              count=count+1
      return count

  string1=input("enter a string: ")
  result=vowel_count(string1)
  print(result)
