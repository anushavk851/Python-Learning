#5. Hospital Patients
 # [Patient ID, Name, Age, Disease, Doctor, Bill]
 # Problems:
  # 1.Print patients above 60 years.
  # 2.Print patients treated by "Dr. Arun".
  # 3.Find the highest bill.
  # 4.Find the total bill amount.
  # 5.Print patients with bills above ₹50,000.
  # 6.Count patients with Diabetes.
  # 7.Print names and diseases.
  # 8.Find the average bill.
  # 9.Print patients below 18 years.
  # 10.Print the patient with the lowest bill.

patients = [[101, "Rahul", 65, "Diabetes", "Dr. Arun", 45000],[102, "Anu", 30, "Fever", "Dr. Meera", 12000],
    [103, "Ravi", 72, "Heart", "Dr. Arun", 85000],[104, "Priya", 15, "Asthma", "Dr. Kiran", 18000],
    [105, "Mohan", 68, "Diabetes", "Dr. Arun", 52000]]
for p in patients:
    if p[2] > 60:
        print(p)
print()#2
for p in patients:
    if p[4] == "Dr. Arun":
        print(p)
print()#3
highest = patients[0]
for p in patients:
    if p[5] > highest[5]:
        highest = p
print("Patient with Highest Bill",highest)
print()#4
total = 0
for p in patients:
    total += p[5]
print("Total Bill Amount:", total)
print()#5
for p in patients:
    if p[5] > 50000:
        print(p)
print()#6
count = 0
for p in patients:
    if p[3] == "Diabetes":
        count += 1
print("Number of Diabetes Patients:", count)
print()#7
for p in patients:
    print(p[1], "-", p[3])
print()#8
average = total / len(patients)
print("Average Bill:", average)
print()#9
for p in patients:
    if p[2] < 18:
        print(p)
print()#10
lowest = patients[0]
for p in patients:
    if p[5] < lowest[5]:
        lowest = p
print("Patient with Lowest Bill",lowest)
