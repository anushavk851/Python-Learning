#Check if the number is palindrome (number reads same in forward and backwards eg 1221 )
  n=int(input("enter the number: "))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  n4=n%10000//1000
  m= (n1*1000)+(n2*100)+(n3*10)+n4
  print(n==m) 
