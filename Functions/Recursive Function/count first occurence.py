#Count the occurence of a chara.
def count_char(s, ch):
    if s == "":
        return 0

    if s[0] == ch:
        return 1 + count_char(s[1:], ch)
    else:
        return count_char(s[1:], ch)

text = "programming"
print("Occurrences:", count_char(text, "m"))
