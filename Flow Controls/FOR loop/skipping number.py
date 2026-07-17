#Count from 1 to 70,skipping multiples of 6.
  n=70
  count=0
  for i in range(1,n+1):
      if i%6==0:
          continue
      count=count+1

  print("total count is: ",count)
