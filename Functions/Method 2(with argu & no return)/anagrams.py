#Write a function that accepts two strings and print whether they are anagrams.
  def anagrams(string1,string2):
      if sorted(string1)==sorted(string2):
              print("Anagram")
      else:
              print("Not Anagram")

  s1=input("enter a string: ")
  s2=input("enter another string: ")
  anagrams(s1,s2)
