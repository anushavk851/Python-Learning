#Reverse a string.
def reverse(s):
    if s == "":
        return ""

    return reverse(s[1:]) + s[0]

text = "Python"
print("Reverse:", reverse(text))
