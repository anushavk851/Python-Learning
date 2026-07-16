#check whether sum of first two digit equals sum of last two digits
  n=int(input("enter a number: "))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  n4=n%10000//1000
  sum1=n4+n3
  sum2=n2+n1
  print(sum1==sum2)
