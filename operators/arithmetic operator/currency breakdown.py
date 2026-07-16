#breakdown currency note to 500,100,50,10,5(using 5 digit number)
  n=int(input("enter the amount of money: ")) #taking 12345 as eg
  n5=n//500
  remaining=n%500  #here after diving by 500 we need to find the remaining amount.so using modulus of 500 .
  n4=remaining//100
  remaining=n%100
  n3= remaining//50
  remaining=n%50
  n2= remaining//10
  remaining=n%10
  n1= remaining//5
  remaining=n%5
  print("number of 500 notes is",n5,)
  print("number of 100 notes is",n4,)
  print("number of 50 notes is",n3,)
  print("number of 10 notes is",n2,)
  print("number of 5 notes is",n1,)
