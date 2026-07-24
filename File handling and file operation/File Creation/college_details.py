# Fields
 # CourseID,CourseName,Department,StudentsEnrolled,CourseFee
# Questions
#1 Read all course records from the file.
#2 Print all CSE courses.
#3 Print courses with a fee greater than 9000.
#4 Print courses having more than 100 students.
#5 Count the number of courses in each department.
#6 Count courses based on student enrollment:
    # Below 80
    # 80–120
    # Above 120
#7 Count courses based on course fee:
    # Below 8000
    # 8000–10000
    # Above 10000
#8 Find the course with the highest fee.
#9 Find the course with the lowest fee.
#10 Find the average course fee.
#11 Find the average number of students enrolled.
#12 Print course names whose fee is between 8000 and 9500.
#13 Find the department having the maximum number of courses.
#14 Calculate the total revenue for each course:
    # Revenue = StudentsEnrolled × CourseFee
#15 Find the course that generates the highest revenue.
#16 Print the details of the course with the minimum enrollment.
#17 Find the total number of students enrolled in all courses.
#18 Print all course names in alphabetical order.

with open(r"C:\Users\ACCURATE\Desktop\college.txt","r") as f:
    data=f.readline()
    college=[]
    while data:
        CourseID,CourseName,Department,StudentsEnrolled,CourseFee=data.strip().split(",")
        college.append([int(CourseID),CourseName,Department,int(StudentsEnrolled),int(CourseFee)])
        data=f.readline()
#1 
    for course in college:
        print(course)
#2
    print()
    for course in college:
        if course[2]=="CSE":
            print(course)
#3
    print()
    for course in college:
        if course[4]>9000:
            print(course[1])
#4
    print()
    for course in college:
        if course[3]>100:
            print(course[1])
#5
    print()
    Department={}
    for course in college:
        if course[2] in Department:
            Department[course[2]]+=1
        else:
            Department[course[2]]=1
    print("number of course in each department: ",Department)
#6
    print()
    stu_enroll={
        "Below 80":0,
        "80-120":0,
        "Above 120":0
    }
    for course in college:
        if course[3]<80:
            stu_enroll["Below 80"]+=1
        elif 80<=course[3]<=120:
            stu_enroll["80-120"]+=1
        else:
            stu_enroll["Above 120"]+=1
    print(stu_enroll)
#7 
    print()
    count_course={
        "below 8000":0,
        "8000-10000":0,
        "above 10000":0
    }
    for course in college:
        if course[4]<8000:
            count_course["below 8000"]+=1
        elif 8000<=course[4]<=10000:
            count_course["8000-10000"]+=1
        else:
            count_course["above 10000"]+=1
    print(count_course)
#8
    print()
    highest=college[0][4]  
    for course in college:
        if course[4]>highest:
            highest=course[4]
    for course in college:
        if highest==course[4]:
            print("course with highest fee: ",course[1])
#9
    print()
    lowest=college[0][4]
    for course in college:
        if course[4]<lowest:
            lowest=course[4]
    for course in college:
        if lowest==course[4]:
            print("course with lowest price is : ",course[1])      
#10
    print()
    total_fee=0
    count=0
    for course in college:
        total_fee+=course[4]
        count=count+1
    print("average course fee is: ",total_fee/count)
#11
    print()
    total_stu=0
    count=0
    for course in college:
        total_stu+=course[3]
        count+=1
    print("average no of student enrolled : ",total_stu//count)
#12
    print()
    for course in college:
        if  8000<course[4]<9500:
            print(course[1])
#13
    print()
    department={}
    for course in college:
        if course[2] in department:
            department[course[2]]+=1
        else:
            department[course[2]]=1
    max_count=0
    max_course=""
    for i in department:
        if department[i]>max_count:
            max_count=department[i]
            max_course=i
    print("department having maximum number of course: ",max_course)
    print("number of course: ",max_count)
#14
    print()
    total_rev=0
    for course in college:
        total_rev=total_rev+(course[3]*course[4])
    print("total revenue is: ",total_rev)
#15
    print()
    highest=0
    highest_course=""
    for course in college:
        total_rev=course[3]*course[4]
        if total_rev>highest:
            highest=total_rev
            highest_course=course[1]
    print(highest_course)
#16
    print()
    minimum=college[0][3]
    for course in college:
        if course[3]<minimum:
            minimum=course[3]
    for course in college:
        if minimum==course[3]:
            print(course)
#17
    print()
    total_stu=0
    for cousre in college:
        total_stu=total_stu+course[3]
    print("total number of student: ",total_stu)
#18
    print()
    lst=[]
    for course in college:
       lst.append(course[1])
    lst.sort()
    for course in lst:
        print(course)
