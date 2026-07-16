#take 5 mark from user out of 20 and find the total then print grade using if elif statements
  sub1=int(input("enter marks for subject1: "))
  sub2=int(input("enter marks for subject2: "))
  sub3=int(input("enter marks for subject3: "))
  sub4=int(input("enter marks for subject4: "))
  sub5=int(input("enter marks for subject5: "))
  total_marks=sub1+sub2+sub3+sub4+sub5
  print("total mark is: ",total_marks)
  if total_marks>=90:
              print("Grade A+")
  elif total_marks>=80:
              print("Grade A")
  elif total_marks>=70:
              print("Grade B+")
  elif total_marks>=60:
              print("Grade B")  
  elif total_marks>=50:
              print("Grade C+")            
  else:
              print("Fail")       
