def simple_interest(principal, rate, time):

    """Calculate simple interest.

    Returns:
        float: The calculated simple interest.
    """

    try:
        interest = (principal * rate * time) / 100  # simple interest formula
        return round(interest, 2) # simple interest
    
    except Exception as e:
        return f"Error in simple interest: {e}"
    

def compound_interest(principal, rate, time):

    """Calculate compound interest.
    
    Returns:
        float: The calculated compound interest.
    """

    try:
        amount = principal * (1 + rate / 100) ** time # compound interest formula
        interest = amount - principal  
        return round(interest, 2) # compound interest
    
    except Exception as e:
        return f"Error in compound interest: {e}"
    
# Main function to run the interest calculator
if __name__ == "__main__":

    print("Interest Calculator")
    print("1. Simple Interest ", " 2. Cmpound Interest", sep="|")

    # user input
    choice = input("Choose an option (1 or 2): ")
    principal = float(input("Principal Amount:"))
    rate = float(input("Rate of Interest:"))
    time = float(input("Time (in years):"))

    # Calculate interest based on user choice
    if choice == '1':
        print(f"Simple interest: {simple_interest(principal, rate, time)}")
    elif choice == '2':
        print(f"Compound interest: {compound_interest(principal, rate, time)}")
    else:
        print("Invalid choice.")
    