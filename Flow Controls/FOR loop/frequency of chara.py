#Write a Python program to count the frequency of each character in a string.
s = input()
visited = ""
for ch in s:
    if ch not in visited:
        count = 0
        
        for c in s:
            if ch == c:
                count = count + 1
        
        print(ch, count)
        visited = visited + ch
