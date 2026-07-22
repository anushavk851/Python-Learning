#write a recursive function to print all element in a list.
def print_list(list,idx=0):
    if idx==len(list):
        return
    else:
        print(list[idx])
        print_list(list,idx+1)
names=["anu","anil","bindu","anusree"]
print_list(names)
