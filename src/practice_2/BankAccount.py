class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):

        if amount > self.__balance or amount < 0:
            raise ValueError("Incorrect value")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
