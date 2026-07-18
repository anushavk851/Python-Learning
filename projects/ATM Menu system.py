#ATM Menu System

#  Features:
  # Check Balance
  # Deposit Money
  # Withdraw Money
  # Exit Option
  
  #Program flow
  
  # Start
  #    |
  # Enter Initial Balance
  #    |
  #    |
  # Show ATM Menu
  #    |
  #    |
  # User Choice?
  #    │
  #    ├── 1 → Check Balance
  #    │
  #    ├── 2 → Deposit → Update Balance
  #    │
  #    ├── 3 → Withdraw → Update Balance
  #    │
  #    ├── 4 → Exit
  #    │
  #    └── Invalid Choice → Show Error
  #    │
  #    |
  # Return to Menu
 

def check_balance(balance):
    print("Your current balance is:  ", balance)


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance = balance + amount
        print("₹", amount, "deposited successfully.")
    else:
        print("Please enter a valid amount.")
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Please enter a valid amount.")
    elif amount <= balance:
        balance = balance - amount
        print("₹", amount, "withdrawn successfully.")
    else:
        print("Insufficient balance.")
    return balance


balance = float(input("Enter your initial balance:  "))

while True:
    print(" ATM MENU ")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance(balance)

    elif choice == "2":
        balance = deposit(balance)

    elif choice == "3":
        balance = withdraw(balance)

    elif choice == "4":
        print("Thank you for using our ATM.")
        break

    else:
        print("Invalid choice. Please try again.")
