#Centered number pyramid
 #          1
 #        1 2 1
 #      1 2 3 2 1
 #    1 2 3 4 3 2 1
n = int(input("Enter number of rows: "))
for i in range(1, n+1):
    # Leading spaces
    for j in range(n-i):
        print(" ", end=" ")

    # Ascending numbers
    for j in range(1, i+1):
        print(j, end=" ")

    # Descending numbers
    for j in range(i-1, 0, -1):
        print(j, end=" ")

    print()
