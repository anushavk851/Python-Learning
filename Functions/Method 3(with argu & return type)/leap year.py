#Write a function that accepts a year and returns whether it is a leap year.
def leap_year(year):
    if year%400==0 or(year%100!=0 and year%4==0):
        return "leap year"
    else:
        return "Not Leapyear"

year1=int(input("enter a year: "))
result=leap_year(year1)
print(result)
