# Count Positive and Negative Numbers
# Create a file integers.txt containing:
#     10
#     -5
#     30
#     -8
#     15
#     -20
# Read the values into a list and count:
 # Positive numbers
 # Negative numbers

# f=open("integers.txt","x")
# f.close()

# with open("integers.txt","a") as f:
#     f.write("10\n")
#     f.write("-5\n")
#     f.write("30\n")
#     f.write("-8\n")
#     f.write("15\n")
#     f.write("-20\n")

with open("integers.txt","r") as f:
    lst=[]
    pve=0
    nve=0
    for i in f:
        lst.append(int(i.strip()))
    for i in lst:
        if i>0:
            pve=pve+1
        elif i<0:
            nve=nve+1
        else:
            continue
    print("number of positive value: ",pve)
    print("number of negative value: ",nve)
