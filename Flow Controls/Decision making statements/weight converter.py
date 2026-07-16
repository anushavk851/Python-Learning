#6 Weight converter (from pounds to weight)
  weight=int(input("enter your weight: "))
  unit=(input("(L)bs or (K)g: "))
  if unit.upper()=="L" :
      weight=weight*0.45
      print(f'you are {weight} kg')
  elif unit.upper()=="K":
      weight=weight/0.45
      print(f'you are {weight}lbs')
  else:
      print("please select either K or L")
