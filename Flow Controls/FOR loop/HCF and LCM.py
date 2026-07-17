#Find the HCF and LCM of 2 numbers.
  n1=int(input("enter first number: "))
  n2=int(input("enter second number: "))
  for i in range(1,min(n1,n2)+1):
      if n1%i==0 and n2%i==0:
          hcf=i
  lcm=(n1*n2)//hcf
  print("HCF of the given numbers is: ",hcf)
  print("LCM of the given numbers is: ",lcm)
