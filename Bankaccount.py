class BankAccount:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_from(self, amount, to_account):
        self.withdraw(amount)
        to_account.deposit(amount)

    def __str__(self):
        return f"BankAccount(id={self.id}, name={self.first_name} {self.last_name}, balance={self.balance})"


def main():
    # Create three bank account objects and print them
    account1 = BankAccount(1, "John", "Doe")
    account2 = BankAccount(2, "Jane", "Doe")
    account3 = BankAccount(3, "Alice", "Smith")

    print("Initial Bank Accounts:")
    print(account1)
    print(account2)
    print(account3)

    # Deposit 100.00 into each bank account object and print them again
    for account in [account1, account2, account3]:
        account.deposit(100.00)

    print("\nBank Accounts after Deposit:")
    print(account1)
    print(account2)
    print(account3)


    try:
        account1.withdraw(50.00)
        print("\nWithdrawal successful from account1.")
    except ValueError as e:
        print(f"\nError: {e}")

    # Withdraw funds from an account without enough funds
    try:
        account2.withdraw(200.00)
        print("Withdrawal successful from account2.")
    except ValueError as e:
        print(f"Error: {e}")


    account3.transfer_from(30.00, account1)


    try:
        account2.transfer_from(150.00, account3)
        print("Transfer successful from account2 to account3.")
    except ValueError as e:
        print(f"Error: {e}")

    # Print the objects again
    print("\nBank Accounts after Transactions:")
    print(account1)
    print(account2)
    print(account3)


if __name__ == "__main__":
    # Call the main function
    main()
