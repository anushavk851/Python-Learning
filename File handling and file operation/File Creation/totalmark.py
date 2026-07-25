#1 Create a file named marks.txt.
 # Store 5 marks entered by the user into the file.
 # Then read the file and display:
    # Total marks
    # Average marks
    # Highest mark
    # Lowest mark
 # Requirements:
    # Use file handling (open, write, read/readlines, close).
    # Take the 5 marks from the user.
    # Do not use exception handling.

# with open("marks.txt","x") as f:
#     pass

# with open("marks.txt","a") as f:
#     m1=input()
#     m2=input()
#     m3=input()
#     m4=input()
#     m5=input()
#     f.write(m1+"\n")
#     f.write(m2+"\n")
#     f.write(m3+"\n")
#     f.write(m4+"\n")
#     f.write(m5+"\n")
# with open("marks.txt","r") as f:
#     f.read()

with open("marks.txt","r") as f:
    lst=[]
    for i in f:
        lst.append(int(i.strip()))

    total_mark=0
    count=0
    highest=lst[0]
    lowest=lst[0]
    for i in lst:
        total_mark+=i
        count=count+1
    print("total mark is: ",total_mark)
    print("average mark is: ",total_mark/count)
    for i in lst:
        if i>highest:
            highest=i
        if i<lowest:
            lowest=i
    print("highest mark is: ",highest)
    print("lowest mark is: ",lowest)
