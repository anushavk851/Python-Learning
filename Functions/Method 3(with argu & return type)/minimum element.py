#write a function that accepts a list of numbers and return the minimum element.
def minimum(list1):
    min=list1[0]
    for i in list1:
        if i<min:
            min=i
    return min

li=list(map(int,input().split()))
result=minimum(li)
print(result)
