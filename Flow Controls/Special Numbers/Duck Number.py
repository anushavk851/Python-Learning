#Duck number-contains at least one 0,but not as first digit(1203).
n=input("enter a number: ")
if '0' in n[1:]:
    print("Duck number")
else:
    print("Not Duck Number")
