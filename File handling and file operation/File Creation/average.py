#Find Average
 # Create a file marks.txt containing:
  # 80
  # 75
  # 90
  # 65
  # 70
# Read the numbers into a list and find the average.

# f=open("mark.txt","x")
# f.close() 

# with open("mark.txt","a") as f:
#   f.write("80\n")
#   f.write("75\n")
#   f.write("90\n")
#   f.write("65\n")
#   f.write("70\n")

with open("mark.txt","r") as f:
  lst=[]
  for i in f:
    lst.append(int(i.rstrip()))
  a=sum(lst)
  b=len(lst)
  print("average mark is: ",a/b)


