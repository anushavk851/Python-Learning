#Count uppercase letters
def count_upper(s):
    if s == "":
        return 0

    if s[0].isupper():
        return 1 + count_upper(s[1:])
    else:
        return count_upper(s[1:])

text = "PyTHon ProGRAMming"
print("Uppercase:", count_upper(text))
