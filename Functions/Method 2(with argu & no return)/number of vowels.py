#Write a function that accepts a string and prints the number of vowels.
  def vowels_count(string):
      count=0
      for ch in string:
          if ch in "aeiouAEIOU":
              count=count+1
      print(count)

  string1=input("enter a string: ")
  vowels_count(string1)
