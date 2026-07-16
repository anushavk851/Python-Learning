#find compound interest(amount=p*(1+(r/100))^t)p is principle, r rate and t is time.amount-p is compound interest
  p=int(input("enter the principle"))
  r=int(input("enter the rate"))
  t=int(input("enter the time"))
  amount=(p*(1+(r/100))**t)
  compound_interest= amount-p
  print("compound interest is: ",compound_interest)
