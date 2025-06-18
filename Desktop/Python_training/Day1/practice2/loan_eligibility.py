# Function to calculate EMI
def calculate_emi(loan_amount, interest_rate, years):

    # Monthly interest rate
    r = interest_rate /12/100  
    n = years * 12  # Total number of months (payments)
    
    # EMI formula 
    emi = (loan_amount * r * (1 + r)**n)/((1 + r)**n-1) 

    return round(emi, 2)  # Round to 2 decimal places


def loan_eligibility(income, emi):

    max_emi = income * 0.4 # Maximum EMI is 40% of income

    # If the emi is less than or equal to the maximum EMI, the user is eligible for the loan
    if emi <= max_emi:
        return "Eligible for loan"
    else:
        return "Not eligible for loan"
    

# main function to run the loan eligibility calculator
if __name__ == "__main__":


    try:
        # user input for loan details 
        loan_amount = float(input("Enter the loan amount: "))
        interest_rate = float(input("Enter the interest rate (annual %): "))
        years = int(input("Enter the loan tenure in years: "))
        income = float(input("Enter your monthly income: "))

        # Calcualte EMI
        emi = calculate_emi(loan_amount, interest_rate, years)
        print("Your EMI is: ", emi)

        # Check loan eligibility
        print(loan_eligibility(income, emi))
    
    except Exception as e:
        print("Please enter valid values", e)

