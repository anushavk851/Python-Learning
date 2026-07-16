#check whether the reverse value of a number is greater than the number
  n=int(input("enter a 3 digit number:"))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  reverse= (n1*100)+(n2*10)+n3
  print(reverse>n)


