# Reverse the List
    # Create a file items.txt containing:
    # 1
    # 2
    # 3
    # 4
    # 5
    # Read the numbers into a list and print the list in reverse order.

# with open("item.txt","x") as f:
#     pass 

# with open("item.txt","a") as f:
#     f.write("1\n")
#     f.write("2\n")
#     f.write("3\n")
#     f.write("4\n")
#     f.write("5\n")

# with open("item.txt","r") as f:
#     lst=[]
#     for i in f:
#         lst.append(int(i.strip()))
#     lst=lst[::-1]
#     print(lst)

#method 2
with open("item.txt","r") as f:
    lst=[]
    for i in f:
        lst.append(int(i.strip()))
    rev=[]
    for i in range(len(lst)-1,-1,-1):
        rev.append(lst[i])
    print(rev)
