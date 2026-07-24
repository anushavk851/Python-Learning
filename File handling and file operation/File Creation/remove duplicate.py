# Remove Duplicate Numbers
# Create a file nums.txt containing:
    # 10
    # 20
    # 10
    # 30
    # 20
    # 40
# Read the numbers into a list and create another list containing only unique numbers.

# with open("nums.txt","x") as f:
#     pass

# with open("nums.txt","a") as f:
#     f.write("10\n")
#     f.write("20\n")
#     f.write("10\n")
#     f.write("30\n")
#     f.write("20\n")
#     f.write("40\n")

# with open("nums.txt","r") as f:
#     lst=[]
#     for i in f:
#         lst.append(int(i.strip()))
#     dup=set(lst)
#     duplicate=list(dup)
#     print(duplicate)

#method2(to get same order)
with open("nums.txt","r") as f:
    lst=[]
    for i in f:
        lst.append(int(i.strip()))
    duplicate=[]
    for i in lst:
        if i not in duplicate:
            duplicate.append(i)
    print(duplicate)
