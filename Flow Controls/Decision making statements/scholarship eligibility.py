#Write a Python program to accept the following details of a student:
 # Name
 # Age
 # Attendance percentage
 # Marks in Mathematics
 # Marks in Science
 # Determine the scholarship eligibility using these rules:
 # 1. If the student's attendance is 75% or more:
 # If both Mathematics and Science marks are 80 or above:
 # If the age is 18 or below, print:
 # Eligible for Full Scholarship
 # Otherwise, print:
 # Eligible for Partial Scholarship
 # Otherwise, print: not eligible
 #otherwise,print marks are low

  name=input("enter your name: ")
  age=int(input("enter your age : "))
  attendence=float(input("enter your attendence percentage: "))
  maths=float(input("enter your mathematics mark: "))
  science=float(input("enter your science mark: "))
  if attendence >= 75:
      if maths>=80 and science >= 80:
          if age<=18:
              print("you are eligible for full scholarship")
          else:
              print("you are eligible for partial scholarship")
      else:
          print("you are not eligible, your marks are low")
  else:
      print("you are not eligible attendence insufficient")
