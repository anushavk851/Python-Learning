#check whether the number is armstrong number(it is a number in which sum of (power of each digit raised to total number of digit) gives the orginal digit)
    #eg 153 1^3+5^3+3^3=153
  n=int(input("enter a 3 digit number: "))
  n1=n%10
  n2=n%100//10
  n3=n%1000//100
  sum=(n1**3)+(n2**3)+(n3**3)
  print(n==sum)
