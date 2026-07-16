#Count the number of vowels in a string.
  def vowels_no():
      string=input("enter a sentence: ")
      count=0
      for i in string:
          if i in "aeiouAEIOU":
              count=count+1
      print(count)

  vowels_no()
