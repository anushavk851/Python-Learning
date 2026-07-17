#Count the number of digits in a number.
n=int(input("enter a number: "))
no_digit=0
while n>0:
  number=n%10
  no_digit=no_digit+1
  n=n//10
print("number of digit in a given number is: ",no_digit)
