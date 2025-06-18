def atm_withdraw(amount):

    """This function handles ATM withdrawal
    
    returns:
        None: Prints the notes to be dispensed"""
    try:
        if amount % 100 != 0:
            print("enter amount multiples of 100.")
        else:
            print("Notes: ")

            note_2000 = amount // 2000 # Calculate number of ₹2000 notes
            amount %= 2000 # Update amount after  ₹2000 notes

            note_500 = amount // 500 # Calculate number of ₹500 notes
            amount %= 500 # Update amount after ₹500 notes

            note_100 = amount // 100 # Calculate number of ₹100 notes
            amount %= 100  # Update amount after ₹100 notes

            # Printing number of each note
            if note_2000 > 0:
                print(f"₹2000 x {note_2000}")
            if note_500 > 0:
                print(f"₹500 x {note_500}")
            if note_100 > 0:
                print(f"₹100 x {note_100}")

    except Exception as e:
        print(f"Error in ATM withdrawal: {e}")

# Main function to run the ATM withdrawal
if __name__ == "__main__":

    # user input
    amount = int(input("Enter amount to withdraw (₹): "))
    atm_withdraw(amount)

    print("Thank you for using the ATM!")
    print("Please collect your cash.")