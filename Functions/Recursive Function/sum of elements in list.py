#Calculate the sum of all element in a list.
def sum_element(list1):
      if len(list1)==0:
            return 0
      else:
            return list1[0]+sum_element(list1[1:])
li=[10,20,30,40,50]
print("sum: ",sum_element(li))
