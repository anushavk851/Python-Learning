#write a function that accept a string and print number of words.
  def words(string):
      no_words=len(string.split())
      print("no of words is: ",no_words)
      
  s=input("enter a sentence: ")
  words(s)
