# Find Second Largest Number
# Create a file marks.txt containing:
    # 85
    # 72
    # 91
    # 67
    # 88
# Read the numbers into a list and find the second largest number.

# with open("marks.txt","x") as f:
#     pass

# with open("marks.txt","a") as f:
#     f.write("85\n")
#     f.write("72\n")
#     f.write("91\n")
#     f.write("67\n")
#     f.write("88\n")

with open("marks.txt","r") as f:
    lst=[]
    for i in f:
        lst.append(int(i.strip()))
    largest=lst[0]
    second=lst[0]
    for i in lst:
        if i>largest:
            second=largest
            largest=i
        elif i>second:
            second=i
    print("second largest mark is: ",second)
