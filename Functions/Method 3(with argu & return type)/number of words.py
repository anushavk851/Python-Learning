#Write a function that accepts a sentence and returns the number of words in it.
def words(string):
    no_words=len(string.split())
    return no_words

string1=input("enter a string: ")
result=words(string1)
print(result)
