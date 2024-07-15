from decimal import Decimal

class Money(Decimal):
    def __new__(cls, v, units='USD'):
        # Create a new instance of Money by calling the __new__ method of the superclass Decimal
        return super(Money, cls).__new__(cls, v)
    
    def __init__(self, v, units='USD'):
        # Initialize the Money instance with a value and units
        self.units = units
    
    def __add__(self, other):
        # Add two Money instances, ensuring they have the same units
        if isinstance(other, Money):
            if self.units == other.units:
                return Money(super().__add__(other), self.units)
            else:
                raise ValueError("Cannot add Money with different units")
        else:
            return Money(super().__add__(Decimal(other)), self.units)
    
    def __sub__(self, other):
        # Subtract two Money instances, ensuring they have the same units
        if isinstance(other, Money):
            if self.units == other.units:
                return Money(super().__sub__(other), self.units)
            else:
                raise ValueError("Cannot subtract Money with different units")
        else:
            return Money(super().__sub__(Decimal(other)), self.units)
    
    def __mul__(self, other):
        # Multiply a Money instance by a scalar
        if isinstance(other, Money):
            raise ValueError("Cannot multiply two Money instances")
        else:
            return Money(super().__mul__(Decimal(other)), self.units)
    
    def __str__(self):
        # Return a string representation of the Money instance, including units
        return super().__str__() + ' ' + self.units

class BankAcct:
    def __init__(self, name, account_number, amount, deposit_interest_rate, withdraw_interest_rate, units='USD'):
        # Initialize the BankAcct instance with account details and balance
        self.balance = Money(amount, units)
        self.name = name
        self.account_number = account_number
        self.deposit_interest_rate = deposit_interest_rate  # Annual deposit interest rate as a percentage
        self.withdraw_interest_rate = withdraw_interest_rate  # Annual withdraw interest rate as a percentage

    def adjust_deposit_interest_rate(self, new_rate):
        # Adjust the deposit interest rate
        self.deposit_interest_rate = new_rate

    def adjust_withdraw_interest_rate(self, new_rate):
        # Adjust the withdraw interest rate
        self.withdraw_interest_rate = new_rate

    def deposit(self, amount):
        # Deposit money into the account
        deposit_money = Money(amount, self.balance.units)
        self.balance += deposit_money

    def withdraw(self, amount):
        # Withdraw money from the account, ensuring sufficient funds
        withdraw_money = Money(amount, self.balance.units)
        if withdraw_money > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= withdraw_money

    def adjust_balance(self, new_balance):
        # Adjust the account balance directly
        self.balance = Money(new_balance, self.balance.units)

    def get_balance(self):
        # Get the current balance of the account
        return self.balance

    def calculate_interest(self, days, for_deposit=True):
        # Calculate interest based on the number of days
        if for_deposit:
            daily_interest_rate = self.deposit_interest_rate / 100 / 365
        else:
            daily_interest_rate = self.withdraw_interest_rate / 100 / 365
        interest = self.balance * daily_interest_rate * days
        return interest

    def __str__(self):
        # Return a string representation of the BankAcct object
        return f"Account Name: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.balance:.2f}\nDeposit Interest Rate: {self.deposit_interest_rate:.2f}%\nWithdraw Interest Rate: {self.withdraw_interest_rate:.2f}%"

def test_bank_acct():
    # Function to test the BankAcct class
    name = input("Enter account holder's name: ")
    acct_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    deposit_rate = float(input("Enter initial deposit interest rate (%): "))
    withdraw_rate = float(input("Enter initial withdraw interest rate (%): "))

    acct = BankAcct(name, acct_number, initial_balance, deposit_rate, withdraw_rate)
    print(acct)

    # Adjust deposit interest rate
    new_deposit_rate = float(input("Enter new deposit interest rate: "))
    acct.adjust_deposit_interest_rate(new_deposit_rate)
    print("\nAfter adjusting deposit interest rate:")
    print(acct)

    # Adjust withdraw interest rate
    new_withdraw_rate = float(input("Enter new withdraw interest rate: "))
    acct.adjust_withdraw_interest_rate(new_withdraw_rate)
    print("\nAfter adjusting withdraw interest rate:")
    print(acct)

    # Adjust balance
    new_balance = float(input("Enter new balance: "))
    acct.adjust_balance(new_balance)
    print("\nAfter adjusting balance:")
    print(acct)

    # Deposit money
    deposit_amount = float(input("Enter amount to deposit: "))
    acct.deposit(deposit_amount)
    print("\nAfter depositing:")
    print(acct)

    # Withdraw money
    withdraw_amount = float(input("Enter amount to withdraw: "))
    acct.withdraw(withdraw_amount)
    print("\nAfter withdrawing:")
    print(acct)

    # Calculate deposit interest
    days = int(input("Enter the number of days to calculate deposit interest: "))
    interest = acct.calculate_interest(days, for_deposit=True)
    print(f"\nDeposit interest for {days} days: ${interest:.2f}")

    # Calculate withdraw interest
    days = int(input("Enter the number of days to calculate withdraw interest: "))
    interest = acct.calculate_interest(days, for_deposit=False)
    print(f"\nWithdraw interest for {days} days: ${interest:.2f}")

    # Get current balance
    balance = acct.get_balance()
    print(f"\nCurrent balance: ${balance:.2f}")

if __name__ == "__main__":
    test_bank_acct()
