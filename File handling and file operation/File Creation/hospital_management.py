# Fields
   # PatientID,Name,Age,Disease,City,Bill
# Questions
#1 Print patients above 60 years.
#2 Print all Diabetes patients.
#3 Print patients from Chennai.
#4 Print patients whose bill exceeds 25,000.
#5 Count patients by disease.
#6 Count patients by city.
#7 Count patients by age group:
    # Below 40
    # 40–60
    # Above 60
#8 Count patients by bill group:
    # Below 10,000
    # 10,000–50,000
    # Above 50,000
#9 Find the patient with the highest bill.
#10 Find the patient with the lowest bill.
#11 Find the average bill amount.
#12 Find the disease with the maximum number of patients.
#13 Print names of patients whose bills are between 20,000 and 40,000.
#14 Find the total hospital revenue.
#15 Print details of the oldest patient.

with open(r"C:\Users\ACCURATE\Desktop\patient.txt","r") as f:
    data=f.readline()
    hospital=[]
    while data:
        PatientID,Name,Age,Disease,City,Bill=data.strip().split(",")
        hospital.append([int(PatientID),Name,int(Age),Disease,City,int(Bill)])
        data=f.readline()
#1  
    for i in hospital:
        if i[2]>60:
            print(i)
#2
    print()
    for i in hospital:
        if i[3]=="Diabetes":
            print(i[1])
#3
    print()
    for i in hospital:
        if i[4]=="Chennai":
            print(i[1])
#4
    print()
    for i in hospital:
        if i[5]>25000:
            print(i)
#5
    print()
    disease={}
    for i in hospital:
        if i[3] in disease:
            disease[i[3]]+=1
        else:
            disease[i[3]]=1
    print(disease)
#6
    print()
    city={}
    for i in hospital:
        if i[4] in city:
            city[i[4]]+=1
        else:
            city[i[4]]=1
    print(city)
#7
    print()
    age={
        "Below 40":0,
        "40-60":0,
        "above 60":0
    }
    for i in hospital:
        if i[2]<40:
            age["Below 40"]+=1
        elif i[2]>60:
            age["above 60"]+=1
        else:
            age["40-60"]+=1
    print(age)
#8
    print()
    bill={
        "below 10000":0,
        "10000-50000":0,
        "above 50000":0
    }
    for i in hospital:
        if i[5]<10000:
            bill["below 10000"]+=1
        elif i[5]>50000:
            bill["above 50000"]+=1
        else:
            bill["10000-50000"]+=1
    print(bill)
#9
    print()
    h_bill=hospital[0][5]
    for i in hospital:
        if i[5]>h_bill:
            h_bill=i[5]
    for i in hospital:
        if h_bill==i[5]:
            print("details of patient with highest bill: ",i)
#10
    print()
    l_bill=hospital[0][5]
    for i in hospital:
        if i[5]<l_bill:
            l_bill=i[5]
    for i in hospital:
        if l_bill==i[5]:
            print("details of patient with lowest bill: ",i)
#11
    print()
    total_bill=0
    count=0
    for i in hospital:
        total_bill+=i[5]
        count+=1
    print("average bill in hospital: ",total_bill/count)
#12
    print()
    disease={}
    for i in hospital:
        if i[3] in disease:
            disease[i[3]]+=1
        else:
            disease[i[3]]=1
    max_disease=""
    max_count=0
    for i in disease:
        if disease[i]>max_count:
            max_count=disease[i]
            max_disease=i
    print("disease with maximum number of patient: ",max_disease)
    print("number of patients: ",max_count)
#13
    print()
    for i in hospital:
        if 20000<i[5]<40000:
            print(i)   
#14
    print()
    sum_bill=0
    for  i in hospital:
        sum_bill=sum_bill+i[5]
    print("total revenue : ",sum_bill)
#15
    print()
    oldest=hospital[0][2]
    for i in hospital:
        if i[2]>oldest:
            oldest=i[2]
    for i in hospital:
        if oldest==i[2]:
            print(i)
