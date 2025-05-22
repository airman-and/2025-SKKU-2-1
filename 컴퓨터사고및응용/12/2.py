class BankAccount:
    def __init__(self, name, number, balance):
        self.balance = balance
        self.name = name
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
class CheckingAccount(BankAccount):
    def __init__(self, name, number, balance): 
        super().__init__(name, number, balance)
        self.withdraw_charge = 10000

    def withdraw(self, amount):
        return BankAccount.withdraw(self, amount + self.withdraw_charge)
    
class SavingsAccount(BankAccount):
    def __init__(self, name, number, balance, interest_rate):
        super().__init__(name, number, balance)
        self.interest_rate = interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def get_initerest_rate(self):

