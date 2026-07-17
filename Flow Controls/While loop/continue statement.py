#Print numbers from 0 to 15 using a while loop. Skip printing the number 8 .

i=-1
while i<15:
    i=i+1
    if i==8:
        continue
    print(i)
