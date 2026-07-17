#Create a simple atm menu using while loop:
 #1 check balance
 #2 Deposit
 #3 withdraw
 #4 exit

balance=float(input("enter your balance amount: "))
while True:
  print("1. Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")
  option=int(input("enter your choice from the above: "))

  if option==1:
     print("your Balance amount is Rs ",balance)

  elif option==2:
     amount=float(input("enter the amount to deposit: "))
     balance=balance+amount
     print("total balance is Rs ",balance)

  elif option==3:
     withdraw=float(input("enter the amount to withdraw: "))
     if withdraw <=balance:
           balance=balance-withdraw
           print("withdraw successful.your balance amount is Rs ",balance)
     else:
           print("insufficent bank balance")

  elif option==4:
     break
  else:
     print("invalid option,please choose any one of the options given")
