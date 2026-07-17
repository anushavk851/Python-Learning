#Write a function that accepts radius of a circle and return its area(pir^2)
  def area_circle(radius):
      area=3.14*(radius**2)
      return area

  r=int(input("enter the radius: "))
  result=area_circle(r)
  print(result)
