class BankAcct:
    def __init__(self, name, account_number, amount, deposit_interest_rate, withdraw_interest_rate):
        """
        Initialize a Bank Account with name, account number, initial amount,
        deposit interest rate, and withdraw interest rate.

        Args:
        - name (str): Account holder's name
        - account_number (str): Account number
        - amount (float): Initial balance amount
        - deposit_interest_rate (float): Annual deposit interest rate as a percentage
        - withdraw_interest_rate (float): Annual withdraw interest rate as a percentage
        """
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.deposit_interest_rate = deposit_interest_rate  # Annual deposit interest rate as a percentage
        self.withdraw_interest_rate = withdraw_interest_rate  # Annual withdraw interest rate as a percentage

    def adjust_deposit_interest_rate(self, new_rate):
        """
        Adjust the deposit interest rate.

        Args:
        - new_rate (float): New deposit interest rate as a percentage
        """
        self.deposit_interest_rate = new_rate

    def adjust_withdraw_interest_rate(self, new_rate):
        """
        Adjust the withdraw interest rate.

        Args:
        - new_rate (float): New withdraw interest rate as a percentage
        """
        self.withdraw_interest_rate = new_rate

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
        - amount (float): Amount to deposit
        """
        self.amount += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account, if sufficient funds are available.

        Args:
        - amount (float): Amount to withdraw
        """
        if amount > self.amount:
            print("Insufficient funds")
        else:
            self.amount -= amount

    def adjust_balance(self, new_balance):
        """
        Adjust the account balance directly.

        Args:
        - new_balance (float): New balance amount
        """
        self.amount = new_balance

    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
        - float: Current balance
        """
        return self.amount

    def calculate_interest(self, days, for_deposit=True):
        """
        Calculate interest based on the number of days.

        Args:
        - days (int): Number of days to calculate interest for
        - for_deposit (bool): True if calculating deposit interest, False for withdraw interest

        Returns:
        - float: Calculated interest amount
        """
        if for_deposit:
            daily_interest_rate = self.deposit_interest_rate / 100 / 365
        else:
            daily_interest_rate = self.withdraw_interest_rate / 100 / 365
        interest = self.amount * daily_interest_rate * days
        return interest

    def __str__(self):
        """
        Return a string representation of the BankAcct object.

        Returns:
        - str: Formatted account information
        """
        return f"Account Name: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}\nDeposit Interest Rate: {self.deposit_interest_rate:.2f}%\nWithdraw Interest Rate: {self.withdraw_interest_rate:.2f}%"

def test_bank_acct():
    """
    Test function to demonstrate the usage of the BankAcct class.
    """
    # Create a new bank account
    name = input("Enter account holder's name: ")
    acct_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    deposit_rate = float(input("Enter initial deposit interest rate (%): "))
    withdraw_rate = float(input("Enter initial withdraw interest rate (%): "))

    acct = BankAcct(name, acct_number, initial_balance, deposit_rate, withdraw_rate)
    print(acct)

    # Adjust the deposit interest rate
    new_deposit_rate = float(input("Enter new deposit interest rate: "))
    acct.adjust_deposit_interest_rate(new_deposit_rate)
    print("\nAfter adjusting deposit interest rate:")
    print(acct)

    # Adjust the withdraw interest rate
    new_withdraw_rate = float(input("Enter new withdraw interest rate: "))
    acct.adjust_withdraw_interest_rate(new_withdraw_rate)
    print("\nAfter adjusting withdraw interest rate:")
    print(acct)

    # Adjust the balance
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

    # Ask user to input the number of days to calculate interest for deposit
    days = int(input("Enter the number of days to calculate deposit interest: "))
    interest = acct.calculate_interest(days, for_deposit=True)
    print(f"\nDeposit interest for {days} days: ${interest:.2f}")

    # Ask user to input the number of days to calculate interest for withdraw
    days = int(input("Enter the number of days to calculate withdraw interest: "))
    interest = acct.calculate_interest(days, for_deposit=False)
    print(f"\nWithdraw interest for {days} days: ${interest:.2f}")

    # Get balance
    balance = acct.get_balance()
    print(f"\nCurrent balance: ${balance:.2f}")

if __name__ == "__main__":
    test_bank_acct()


