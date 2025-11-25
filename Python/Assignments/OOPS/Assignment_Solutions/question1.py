class BankAccount:
    def __init__(self, acc_no, owner_name, balance):
        self.acc_no = acc_no
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Low balance.")

    def get_balance(self):
        return self.balance
    

ac1 = BankAccount("24609691110", "Ritik", 1000)

ac1.withdraw(2500)  
