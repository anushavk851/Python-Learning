#14 Accept the purchase amount and membership status(yes/no).
 #if purchase amount is above 5000
 #member-20% discount
 #non member-10%discount
 #otherwise(less than 5000)-member=5% discount
 #non member- no discount,display the final amount

  amount=int(input("enter the purchase amount: "))
  membership=input("are you a member?(yes/no): ").lower()
  if amount>5000 :
      if membership=="yes":
      discount=amount*20/100
      amount=amount-discount
      print("final amount is : ",amount)
      else:
      discount=amount*10/100
      amount=amount-discount
      print("final amount is: ",amount)
  else:
      if membership== "yes":
      discount=amount*5/100
      amount=amount-discount
      print("final amount is: ",amount)
      else:
      discount=0
      print("final amount is: ",amount)
