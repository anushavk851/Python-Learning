#check whether sum of digits is greater than product of digits
  n=int(input("enter a 3 digit number: "))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  sum=n1+n2+n3
  product=n1*n2*n3
  print(sum>product)
