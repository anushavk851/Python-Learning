#Print a inverted pyramid.
n=int(input("enter a value: "))
for i in range(n,0,-1):
  print(" "*(n-i)+"* "*i)
