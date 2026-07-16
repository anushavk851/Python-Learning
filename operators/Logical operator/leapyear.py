#check whether the given year is leap year(2 ways to find it 
  1 divisible by 4  
  2 not divisible by 100 but divisible by 400)
  n=int(input("enter any year: "))
  print(n%4==0 or ((n%100==0) and (n%400==0)))
