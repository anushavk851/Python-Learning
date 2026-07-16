#Check whether the year is Leap year or not
  year=int(input("enter any year: "))
  if year%4==0 or (year%100!=0 and year%400==0):
      print("it is leap year")
  else:
      print("not a leap year")
