#Reverse a n-Digit Number (12345)
  n=int(input("enter a 5 digit number ",  ))
  n1=n%10
  n2=((n%100))//10
  n3=((n%1000))//100
  n4=((n%10000))//1000
  n5=((n%100000))//10000
  num= (n1*10000)+(n2*1000)+(n3*100)+(n4*10)+n5
  print("the reversed output is: ", num)
