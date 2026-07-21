#1 employee details of 7 people.
 # 1) find id,fname,lname ,age,proffesion,location of employees where age>25
 # 2) age==27, fname,lname,age
 # 3)python prof--> fname,lname,age,location
 # 4) age above 24 and profession python return full details
 # 5)find total salary of all employees

employees=[[1,"Anusha", "Anilkumar", 24, "Data Scientist", "Calicut", 30000],
        [2,"Anusree", "Viswanath", 26, "Data Analyst", "kochi", 45000],
        [3,"priya", "sharma", 23, "Human Resource", "bangalore", 25000],
        [4,"kousalya", "Guruprasad", 27, "sales associate", "kengeri", 30000],
        [5,"ananya", "sivadas", 34, "python", "calicut", 60000],
        [6,"sai", "bhuvan", 25, "python", "pune", 65000],
        [7,"ashthosh", "behara", 28, "software engineer", "goa", 55000]] 
print("")#1
for i in employees:
    if i[3]>25:
        print(i[:])
print("")#2
for i in employees:
    if i[3]==27:
        print(i[1:4])
print("")#3
for i in employees:
    if i[4]=="python":
        print(i[1], i[2], i[3], i[5])
print("")#4
for i in employees:
    if i[3]>24 and i[4]=="python":
        print(i[:])
print("")#5
total=0
for i in employees:   
    total=total+i[6]
print("total salary of employees is : ",total)


