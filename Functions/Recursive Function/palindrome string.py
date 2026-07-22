#check a string is palindrome 
def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False
    else:
      return palindrome(s[1:-1])
text = "madam"
if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
