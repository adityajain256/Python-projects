class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = new_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount # Using the setter
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount # Using the setter
        else:
            raise ValueError("Invalid withdrawal amount.")

# Example Usage
account = BankAccount(20000)

print("Initial balance:", account.balance)

account.deposit(5000)
print("Balance after deposit:", account.balance)

account.withdraw(3000)
print("Balance after withdrawal:", account.balance)

try:
    account.withdraw(25000)  # Attempting to withdraw more than the balance
except ValueError as e:
    print(e)

try:
    account.balance = -1000  # Attempting to set a negative balance
except ValueError as e:
    print(e)