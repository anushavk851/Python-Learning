#check whether the middle digit is larger.
  n=int(input("enter any 3 digit numbers :,"))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  print(n1<n2 and n2>n3)
