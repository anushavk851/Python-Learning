#find the sum of digits and product of digits (use 4 digit number)
  n=int(input("enter any 4 digit number:" ))
  n1=n%10
  n2=((n%100))//10
  n3=((n%1000))//100
  n4=((n%10000))//1000
  print("sum of digit is :",(n1+n2+n3+n4))
  print("product of digits is:",(n1*n2*n3*n4))
