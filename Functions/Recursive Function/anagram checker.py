#Check whether two strings are anagram without using built-in sorting.
def remove_char(s, ch):
    if s == "":
        return ""
    if s[0] == ch:
        return s[1:]
    else:
        return s[0] + remove_char(s[1:], ch)

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if s1 == "":
        return True
    if s1[0] not in s2:
        return False
    else:
       return anagram(s1[1:], remove_char(s2, s1[0]))

str1 = "listen"
str2 = "silent"
if anagram(str1, str2):
    print("Anagram")
else:
    print("Not Anagram")
