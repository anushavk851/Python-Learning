#Personal Finance & Expense Management System
    # Features
    # 1. Add Income
    # 2. Add Expense
    # 3. View Transactions
    # 4. Search Transactions
    # 5. Total Income
    # 6. Total Expenses
    # 7. Current Balance
    # 8. Category-wise Expenses
    # 9. Monthly Report
    # 10. Save Report

#program flow
# finance_project/
# │
# ├── main.py
# ├── transactions.txt
# └── reports.txt

# Personal Finance & Expense Management System
from datetime import datetime

class Transaction:
    def __init__(self, transaction_type, category, amount, description):
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.description = description
        self.date = datetime.now()

    def display(self):
        print("-"*40)
        print("Type        :", self.transaction_type)
        print("Category    :", self.category)
        print("Amount      :", self.amount)
        print("Description :", self.description)
        print("Date        :", self.date.strftime("%d-%m-%Y"))

class FinanceManager:
    def __init__(self):
        self.transactions=[]

    def add_income(self):
        category=input("Enter income category: ")
        amount=float(input("Enter amount: "))
        if amount<=0:
            print("Amount must be greater than zero.")
            return
        description=input("Enter description: ")
        t=Transaction("Income",category,amount,description)
        self.transactions.append(t)
        self.save_transaction(t)
        print("Income added successfully.")

    def add_expense(self):
        category=input("Enter expense category: ")
        amount=float(input("Enter amount: "))
        if amount<=0:
            print("Amount must be greater than zero.")
            return
        description=input("Enter description: ")
        t=Transaction("Expense",category,amount,description)
        self.transactions.append(t)
        self.save_transaction(t)
        print("Expense added successfully.")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions.")
            return
        for t in self.transactions:
            t.display()

    def search_transaction(self):
        k=input("Enter category/description to search: ").lower()
        found=False
        for t in self.transactions:
            if k in t.category.lower() or k in t.description.lower():
                t.display(); found=True
        if not found:
            print("No matching transaction.")

    def total_income(self):
        print("Total income:",sum(t.amount for t in self.transactions if t.transaction_type=="Income"))

    def total_expense(self):
        print("Total expenses:",sum(t.amount for t in self.transactions if t.transaction_type=="Expense"))

    def balance(self):
        income=sum(t.amount for t in self.transactions if t.transaction_type=="Income")
        expense=sum(t.amount for t in self.transactions if t.transaction_type=="Expense")
        print("Current balance:",income-expense)

    def category_report(self):
        d={}
        for t in self.transactions:
            if t.transaction_type=="Expense":
                d[t.category]=d.get(t.category,0)+t.amount
        if not d:
            print("No expense records.")
            return
        print("\nCATEGORY-WISE EXPENSES")
        for k,v in d.items():
            print(k,":",v)

    def monthly_report(self):
        m=input("Enter month number (01-12): ")
        y=input("Enter year (YYYY): ")
        income=expense=0
        for t in self.transactions:
            if t.date.strftime("%m")==m and t.date.strftime("%Y")==y:
                if t.transaction_type=="Income": income+=t.amount
                else: expense+=t.amount
        if income==0 and expense==0:
            print("No transactions found.")
            return
        print("\nMONTHLY REPORT")
        print("Income:",income)
        print("Expense:",expense)
        print("Balance:",income-expense)

    def save_transaction(self,t):
        with open("transactions.txt","a") as f:
            f.write(f"{t.date.strftime('%d-%m-%Y')}|{t.transaction_type}|{t.category}|{t.amount}|{t.description}\n")

    def save_report(self):
        income=sum(t.amount for t in self.transactions if t.transaction_type=="Income")
        expense=sum(t.amount for t in self.transactions if t.transaction_type=="Expense")
        with open("reports.txt","a") as f:
            f.write("\n========== REPORT ==========\n")
            f.write("Generated: "+datetime.now().strftime("%d-%m-%Y %H:%M:%S")+"\n")
            f.write(f"Total Income: {income}\nTotal Expense: {expense}\nBalance: {income-expense}\n")
        print("Report saved.")

    def load_transactions(self):
        self.transactions.clear()
        with open("transactions.txt","a+") as f:
            f.seek(0)
            for line in f:
                data=line.strip().split("|")
                if len(data)==5:
                    t=Transaction(data[1],data[2],float(data[3]),data[4])
                    t.date=datetime.strptime(data[0],"%d-%m-%Y")
                    self.transactions.append(t)

def menu():
    m=FinanceManager(); m.load_transactions()
    while True:
        print("\n1.Add Income\n2.Add Expense\n3.View Transactions\n4.Search\n5.Total Income\n6.Total Expense\n7.Current Balance\n8.Category-wise Expenses\n9.Monthly Report\n10.Save Report\n11.Exit")
        c=input("Enter choice: ")
        if c=="1": m.add_income()
        elif c=="2": m.add_expense()
        elif c=="3": m.view_transactions()
        elif c=="4": m.search_transaction()
        elif c=="5": m.total_income()
        elif c=="6": m.total_expense()
        elif c=="7": m.balance()
        elif c=="8": m.category_report()
        elif c=="9": m.monthly_report()
        elif c=="10": m.save_report()
        elif c=="11": break
        else: print("Invalid choice.")

menu()
