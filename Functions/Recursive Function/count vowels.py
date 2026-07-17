#Count vowels in a string.
def vowels_count(string):
    if string=="":
        return 0
    elif string[0] in "aeiouAEIOU":
        return 1+vowels_count(string[1:]) 
    else:
        return vowels_count(string[1:])   

text=input("enter a text: ")    
print(vowels_count(text))
