#find sum of squares of digits. lets take 5 digit number 12345
  n=int(input("enter a 5 digit number :"))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  n4=n%10000//1000
  n5=n%100000//10000
  sum=(n1**2)+(n2**2)+(n3**2)+(n4**2)+(n5**2)
  print("the sum of squares of digits is", sum )
