#21 Write a function that accepts two numbers and return True if they are anagrams,otherwise False. (same in case of string as we are taking numbers as string)
def anagrams(n1,n2):
    if len(n1)!=len(n2):
        return False
    else:
        freq1={}
        freq2={}
        for i in n1:
            if i in freq1:
                freq1[i]=freq1[i]+1
            else:
                freq1[i]=1
        for i in n2:
            if i in freq2:
                freq2[i]=freq2[i]+1
            else:
                freq2[i]=1
        if freq1==freq2:
            return True
        else:
            return False

n1=input("enter a value: ")
n2=input("enter a value: ")
result=anagrams(n1,n2)
print(result)
