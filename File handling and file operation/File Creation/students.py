# Fields:
# rollno, name, branch, age, city, marks
# Problems
# 1 Print the names of all CSE students.
# 2 Print students whose age is above 20.
# 3 Print students whose age is between 19 and 21.
# 4 Print students from Bangalore.
# 5 Print students from Hyderabad with marks above 90.
# 6 Print ECE students with their names and marks.
# 7 Print students from Chennai whose age is above 21.
# 8 Print students who scored more than 80 marks.
# 9 Print students who scored below 70 marks.
# 10 Print students from Mysore with their branch.
# 11 Count students in each branch.
# 12 Count students from each city.
# 13 Count students in these mark groups:
#    Below 70 
#    70–85
#    Above 85
# 14 Find the student with the highest marks.
# 15 Find the average marks of all students.


with open(r"C:\Users\ACCURATE\Desktop\students.txt","r") as f:
    data=f.readline()
    student=[]
    while data:
        rollno, name, branch, age, city, marks =data.strip().split(",")
        student.append([int(rollno),name, branch, int(age), city, int(marks)])
        data=f.readline()
        
#1
    for std in student:
        if std[2]=="CSE":
            print(std[1])
#2
    print()
    for std in student:
        if std[3]>20:
            print(std)
#3
    print()
    for std in student:
        if 19<=std[3]<=21:
            print(std)
#4
    print()
    for std in student:
        if std[4]=="Bangalore":
            print(std)
#5
    print()
    for std in student:
        if std[4]=="Hyderabad" and std[5]>90:
            print(std[1])
#6
    print()
    for std in student:
        if std[2]=="ECE":
            print(std[1],std[5])
#7
    print()
    for std in student:
        if std[4]=="Chennai" and std[3]>21:
            print(std)
#8
    print()
    for std in student:
        if std[5]>80:
            print(std)
#9
    print()
    for std in student:
        if std[5]<70:
            print(std)
#10
    print()
    for std in student:
        if std[4]=="Mysore":
            print(std[1],std[2])
#11
    print()
    branch={}
    for std in student:
        if std[2] in branch:
            branch[std[2]]=branch[std[2]]+1
        else:
            branch[std[2]]=1
    print(branch)
#12
    print()
    city={}
    for std in student:
        if std[4] in city:
            city[std[4]]+=1
        else:
            city[std[4]]=1
    print(city)     
#13
    print()
    mark_group={
        "Below 70":0,
        "70-85":0,
        "Above 85":0
    }
    for std in student:
        mark=std[5]
        if mark<70:
            mark_group["Below 70"]+=1
        elif 70<=mark<=85:
            mark_group["70-85"]+=1
        else:
            mark_group["Above 85"]+=1  
    print(mark_group)
#14
    print()
    highest=student[0][5]
    for std in student:
        if std[5]>highest:
            highest=std[5]
    print("highest mark is : ",highest)
#15
    print()
    total_mark=0
    count=0
    for std in student:
        total_mark=total_mark+std[5]
        count=count+1
    print("average mark is: ",total_mark/count)
        
