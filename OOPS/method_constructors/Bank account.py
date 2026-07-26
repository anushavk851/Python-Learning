#5 Bank Account
 # Create a BankAccount class.
 # Attributes: account_holder, account_number, balance
 # Methods:
  # deposit()
  # withdraw()
  # display_balance()
class BankAccount:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance
    def Deposit(self):
        deposit=float(input("enter the amount to deposit: "))
        print(f'Rs {deposit} deposited successfuly')
        self.balance=self.balance+deposit
        print("your current bank balance is: ",self.balance)
    def Withdraw(self):
        withdraw=float(input("enter the amount to withdraw: "))
        if withdraw>self.balance:
            print("insufficient bank balance")
        else:
            print(f'amount {withdraw} withdrawn successfully')
            self.balance=self.balance-withdraw
            print("your current bank balance is: ",self.balance)
    def Balance(self):
        print("your account balance is: ",self.balance)
b1=BankAccount("anusha",1234567,12000)
b1.Balance()
b1.Withdraw()
b1.Deposit()
