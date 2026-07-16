#Take a character from the user and check whether it is a vowel or consonent       
  chara=input("enter a character: ").lower()
  vowels=["a","e","i","o","u"]
  if chara in vowels :
      print("it is a vowel")
  else:
      print("it is consonent")
