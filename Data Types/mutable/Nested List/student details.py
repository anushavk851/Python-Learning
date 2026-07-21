#2 Student details
 # [Roll No, Name, Age, Course, City, Marks]
 # Problems:
  # 1.Print students who scored above 80.
  # 2.Print students from Kochi.
  # 3.Print names of students whose age is below 20.
  # 4.Find the highest marks.
  # 5.Find the lowest marks.
  # 6.Find the average marks.
  # 7.Count students from Bangalore.
  # 8.Print students whose course is "Python".
  # 9.Print the topper's full details.
  # 10.Print students with marks between 60 and 90.

students=[[1,"Anu", 24,"python", "calicut",60],[2,"Anagha", 23,"python", "calicut",90],
          [3,"haritha", 19,"java", "kochi",75],[4,"vishnu", 20,"Data Science", "bangalore",56],
          [5,"sreerag", 18,"java", "kochi",95],[6,"anunanda", 19,"python", "calicut",96],
          [7,"athul", 22,"C++", "calicut",88],[8,"safna", 21,"C++", "palakkad",79]]
#1
for stu in students:
    if stu[5]>80:
        print(stu[:])
print()#2
for stu in students:
    if stu[4]=="kochi":
        print(stu[:])
print()#3
for stu in students:
    if stu[2]<20:
        print(stu[1],end="  ")
print()#4
highest=students[0][5]
for stu in students:
    if stu[5]>highest:
        highest=stu[5]
print("highest mark is: ",highest)
print()#5
lowest=students[0][5]
for stu in students:
    if stu[5]<lowest:
        lowest=stu[5]
print("lowest mark is: ",lowest)
print()#6
total=0
count=len(list(students))
for stu in students:
    total=total+stu[5]
print("average mark is: ",total/count)
print()#7
count=0
for stu in students:
    if stu[4]=="bangalore":
        count=count+1
print(count)
print()#8
for stu in students:
    if stu[3]=="python":
        print(stu[:])
print()#9
highest=students[0][5]
for stu in students:
    if stu[5]>highest:
        highest=stu[5]
for stu in students:
    if stu[5]==highest:
        print("detail of topper: ",stu)
print()#10
for stu in students:
    if 60<=stu[5]<=90:
        print(stu)
