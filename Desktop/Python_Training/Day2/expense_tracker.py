
def add_expense(expenses, amount):
    """Add amount to the expenses list.
    Returns:
        None: Appends amount to expenses list.
    """
    
    expenses.append(amount)

def summary(month, expenses):

    """Prints total and average of expenses.
    Returns:
        None: Prints total and average expenses.
    """

    total = sum(expenses)   # Calculate total expenses
    average = total / len(expenses) # Calculate average expenses

    print(f'Total: ₹{total}')
    print(f'Average: ₹{average:.2f}')

# Main function to run  expense tracker
if __name__ == "__main__":

    expenses = [] # List to store expenses

    # Loop to take user input
    while True:

        month = input("Month (or q to quit):")

        if month == 'q':
            break
        else:

            # User input
            try:
                amount = float(input(f"Expense Amount {month}: ₹")) 
                add_expense(expenses, amount)

            except ValueError:
                print("Invalid amount.")

    # Print summary of expenses
    summary(month, expenses) 

