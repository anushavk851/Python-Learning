#1. Dancer prof, frame, Iname,
#2 Age above  23  foane. Iname, age, prof
#3 Age range 25 to 40 fname. Iname, age, prof
#4 india work, fname, Iname, age, prof
#5 india work and age above 38 fname. lname, age
#6. india work and pro Dancer frame. lname, age
#7 Pilot prof frame. Iname, age
#8 Pilot prof and age above 40 fname, lname, age
#9 us work fname, name, age
#10 us work and age above 45 frame. lname, age
#11. Each profession count
#12 Each Location count
#13 Each Age group count

with open(r"C:\Users\ACCURATE\Desktop\employees (1).txt","r") as f:
    employees=[]
    data=f.readline()
    while data:
        empid, fname, lname, age, prof, location= data.strip().split(",")
        employees.append([empid, fname, lname, int(age), prof, location])
        data=f.readline()
#1
    for emp in employees:
        if emp[4]=="Dancer":
            print(emp[1],emp[2])
#2
    print()
    for emp in employees:
        if emp[3]>23:
            print(emp[1:5])
#3
    print()
    for emp in employees:
        if 25<=emp[3]<=40:
            print(emp[1:5])
#4
    print()
    for emp in employees:
        if emp[5]=="India":
            print(emp[1:5])
#5
    print()
    for emp in employees:
        if emp[5]=="India" and emp[3]>38:
            print(emp[1:4])
#6
    print()
    for emp in employees:
        if emp[5]=="India" and emp[4]=="Dancer":
            print(emp[1:4])
#7  
    print()
    for emp in employees:
        if emp[4]=="Pilot":
            print(emp[1:4])
#8
    print()
    for emp in employees:
        if emp[3]>30 and emp[4]=="Pilot":
            print(emp[1:4])
#9
    print()
    for emp in employees:
        if emp[5]=="USA":
            print(emp[1:4])
#10
    print()
    for emp in employees:
        if emp[5]=="USA" and emp[3]>45:
            print(emp[1:4])
#11
    print()
    prof_count={}
    for emp in employees:
        if emp[4] in prof_count:
            prof_count[emp[4]]+=1
        else:
            prof_count[emp[4]]=1
    print("frequency of profession: ",prof_count)
#12
    print()
    loc_count={}
    for emp in employees:
        if emp[5] in loc_count:
            loc_count[emp[5]]+=1
        else:
            loc_count[emp[5]]=1
    print("frequency of location: ",loc_count)
#13 
    print()
    age_group={
      "20-29":0,
      "30-39":0,
      "40-49":0,
      "50-59":0,
      "60+":0
    }
    
    for emp in employees:
        age=emp[3]
        if 20 <= age<=29:
            age_group["20-29"]+=1
        elif 30<=age<=39:
            age_group["30-39"]+=1
        elif 40<=age<=49:
             age_group["40-49"]+=1
        elif 50<=age<=59:
            age_group["50-59"]+=1
        else:
            age_group["60+"]+=1
    print("frequency of age group: ",age_group)
