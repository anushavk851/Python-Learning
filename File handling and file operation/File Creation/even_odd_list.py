# Separate Even and Odd Lists
# Create a file digits.txt containing:
    # 11
    # 24
    # 35
    # 42
    # 57
    # 60
# Read the numbers into a list and create:
 # even_list
 #odd_list

# with open("digits.txt","x") as f:
#     pass

# with open("digits.txt","a") as f:
#     f.write("11\n")
#     f.write("24\n")
#     f.write("35\n")
#     f.write("42\n")
#     f.write("57\n")
#     f.write("60\n")
#     f.write("1\n")

with open("digits.txt","r") as f:
    lst=[]
    for i in f:
        lst.append(int(i.strip()))
    even=[]
    odd=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("even list: ",even)
    print("odd list: ",odd)
