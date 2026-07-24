# Find Highest and Lowest
    # Create a file scores.txt containing:
    #     45
    #     78
    #     99
    #     62
    #     81
    # Store the numbers in a list and print:
    # The list
    # Highest number
    # Lowest number
    # Total even numbers
    # Total odd numbers

# f=open("scores.txt","x")
# f.close()

# with open("scores.txt","a") as f:
#     f.write("45\n")
#     f.write("78\n")
#     f.write("99\n")
#     f.write("62\n")
#     f.write("81\n")

with open("scores.txt","r") as f:
    lst=[]
    even=0
    odd=0
    for i in f:
        lst.append(int(i.strip()))
        
    highest=lst[0]
    lowest=lst[0]
    for i in lst:
        if highest<i:
            highest=i
        if lowest>i:
            lowest=i
    for i in lst:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
            
    print(lst)
    print("highest value is : ",highest)
    print("lowest value is : ",lowest)
    print("number of even numbers: ",even)
    print("number of odd numbers: ",odd)
