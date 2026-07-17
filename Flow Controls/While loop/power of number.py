#Print power of 2 upto 1024
n=int(input("enter a value: "))
i=0
power=1
while power<n:
  power=2**i
  print(power,end=" ")
  i=i+1
