#Automorphic number-eg 25(25^2=625,ends with 25).
n=int(input("enter a number: "))
square=n*n
if str(square).endswith(str(n)):
    print("Automorphic")
else:
    print("Not Automorphic")
