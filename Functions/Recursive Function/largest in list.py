#Find the largest element in a list using recursion.
def largest(list1):
    if len(list1)==1:
        return list1[0]
    elif list1[0]>largest(list1[1:]):
        return list1[0]
    else:
        return largest(list1[1:])
    
li=list(map(int,input().split()))
print(largest(li))
