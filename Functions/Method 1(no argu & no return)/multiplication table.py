#Print multiplication table of a number
  def multiplication():
      n=int(input("enter a number: "))
      for i in range(1,11):
          print(f'{i} x {n} = {i*n}')

  multiplication()
