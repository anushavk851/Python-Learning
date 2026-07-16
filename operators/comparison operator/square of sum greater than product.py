#check whether square of sum if greater than product.
  n=int(input("enter a 3 digit number: "))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  product=n1*n2*n3
  square_of_sum=(n1+n2+n3)**2
  print(square_of_sum>product)
