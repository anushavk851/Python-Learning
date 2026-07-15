
#PYTHON STRING ANALYZER.
#Features:
 #reverse a string.
 #check palindrome.
 #check anagrams.
 #count vowels.
 #count consonants.
 #count uppercase and lowercse letters
 #Displaying characters frequency.
 #count words.
 #count digits and special characters.
 #find the longest and shortest word.
 #counting how many times a particular character appears.
 #Displaying string in upper and lowercase
 #Removing duplicate character while preserving order


text=input("enter a string: ")

#reversing a string
reverse=text[::-1]
print("reversed string: ",reverse)

#palindrome
if text==reverse:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")


#Count of(Vowels,Consonants,Digits and special character)
vowels=0
consonants=0
digits=0
special=0
for ch in text:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowels+=1
        else:
            consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch!=" ":
        special+=1
print("Number of vowels: ",vowels)
print("Number of Consonants: ",consonants)
print("Number of Digits: ",digits)
print("Number of special Character: ",special)


#Uppercase and Lowercase count
upper=0
lower=0
for ch in text:
    if ch.isupper():
        upper+=1
    elif ch.lower():
        lower+=1
print("No of uppercase: ",upper)
print("No of lowercase: ",lower)


#Character Frequency
freq={}
for ch in text:
    if ch!=" ":
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
print("Frequency of each characters are: ",freq)


#count words
words=text.split()
print("Words Count: ",len(words))


#longest and shortest word in the string
if len(words)>0:
    longest=words[0]
    shortest=words[0]
    for ch in words:
        if len(ch)>len(longest):
            longest=ch
        if len(ch)<len(shortest):
            shortest=ch
    print("longest word is: ",longest)
    print("shortest word is: ",shortest)


#Count Particular Character
character=input("enter a character to count: ")
count=0
for ch in text:
    if ch==character:
        count+=1
print("Number of ",character,"present in string is: ",count)


#Uppercase and lowercase string
print("uppercase string: ",text.upper())
print("lowercase string: ",text.lower())


#Removing Duplicate Characters
result=" "
for ch in text:
    if ch not in result:
        result+=ch
print("String after removing duplicate characters: ",result)


#anagram checking
text2=input("enter another string: ")
s1=text.replace(" ","").lower()
s2=text2.replace(" ","").lower()

if sorted(s1)==sorted(s2):
    print("its an anagram")
else:
    print("it's not an anagram")

