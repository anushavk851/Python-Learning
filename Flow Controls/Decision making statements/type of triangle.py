#Check the type of triangle(equilateral(all side equal),isosceles(any two side equal) or scalene)
  side1=int(input("enter the lenght of side 1: "))
  side2=int(input("enter the lenght of side 2: "))
  side3=int(input("enter the lenght of side 3: "))
  if side1==side2==side3:
      print("it's a equilateral triangle")
  elif side1==side2 or side2==side3 or side3==side1:
      print("it's a isosceles triangle")
  else:
      print("it's a scalene triangle")
