class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def calculate_interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.08):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Calculated interest: ${interest}")
        return interest





savings_account = SavingsAccount(account_number="1", balance=1000)
savings_account.deposit(500)
savings_account.calculate_interest()


