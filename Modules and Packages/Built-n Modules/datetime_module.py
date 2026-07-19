import datetime

d = datetime.date(2026, 7, 19)
t = datetime.time(10, 30, 45)
dt = datetime.datetime(2026, 7, 19, 10, 30)
td = datetime.timedelta(days=5)
tz = datetime.timezone.utc

print(d)
print(t)
print(dt)
print(td)
print(tz)

# Import modules(10 function/method)

print("1. datetime.now():", datetime.datetime.now())             #datetime.now()-Returns current date and time.
print("2. datetime.today():", datetime.datetime.today())         #datetime.today()-Returns today's date and time.
print("3. date.today():", datetime.date.today())                 #date.today()-Returns today's date.

date_time=input("enter date and time (dd-mm-yyyy  hh:mm:ss): ")  #sample input 18-07-2026 10:30:40
dt = datetime.datetime.strptime(date_time, "%d-%m-%Y %H:%M:%S")  #datetime.strptime()-Converts a string into a date/time object.
print("4. datetime.strptime():", dt)

print("5. datetime.strftime():", dt.strftime("%A, %d %B %Y"))    #datetime.strftime()-Converts date/time into a formatted string.

combined = datetime.datetime.combine(datetime.date.today(), datetime.time(10,15))
print("6. datetime.combine():", combined)                        #datetime.combine()-Combines a date and time into one object.

year=int(input("enter a year: "))
print("7. datetime.replace():", combined.replace(year))          #datetime.replace()-Replaces specified values in date/time.

timestamp = datetime.datetime.now().timestamp()                  #timestamp() is number of seconds that have passed since jan 1 1970
print("8. datetime.timestamp():", timestamp)

#datetime.fromtimestamp() converts the timestamp back into normal date and time
print("9. datetime.fromtimestamp():", datetime.datetime.fromtimestamp(timestamp))

days=int(input("enter the days: "))
delta = datetime.timedelta(days) #timedelta() used to add or subtract a duration of time(days,hours,minutes,seconds.etc) from a date or time
print("10. timedelta():", datetime.datetime.now() + delta)

