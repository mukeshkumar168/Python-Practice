class bank:

    """Bank Account Class
    Methods:
        deposit(amount): Deposits account.
        withdraw(amount): Withdraws amount if sufficient funds are available.
        get_balance(): Returns current balance 
    """

    def __init__(self, balance=0): # private variable for balance
        self.__balance = balance

    
    def deposit(self, amount):

        """Function allows to Deposits amount
        Returns:
            str: Updated balance
        """
        
        if amount > 0:
            self.__balance += amount    # add amount to balance
            print(f"Deposited: {amount}")
            return f'Balance: {self.__balance}'
        else:   
            print("Amount must be positive")


    def withdraw(self, amount):

        """Function allows to Withdraw amount
        Returns:
            str: Updated balance or insufficient funds message
        """

        if 0 < amount <= self.__balance:    # checks if amount is positive and less than or equal to balance
            self.__balance -= amount     # subtract amount from balance
            print(f"Withdrawn: {amount}")
            return f'Balance: {self.__balance}'
        else:
            print("Insufficient funds")

    def get_balance(self):      # gets current balance
        return self.__balance
    
# Main function 
if __name__ == "__main__":
    
    print("===Welcome to Bank Account System===")
    bank_account = bank()   # object for bank account


    while True:

        try:
            print('-----------------')
            print("1. Deposit Money\n2.withdraw Money\n3.Check Balance\n4.Exit")
            print('-----------------')
            choice = int(input("Enter your choice: "))

            # Handle user choices
            if choice == 1:
                amount = float(input("Enter amount to deposit: "))
                print(bank_account.deposit(amount))
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                print(bank_account.withdraw(amount))
            elif choice == 3:
                print(f"Current Balance: {bank_account.get_balance()}")
            elif choice == 4:
                print("Exiting system.")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print(f'error in bank {e}')
        