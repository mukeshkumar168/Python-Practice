# import necessary libraries
from datetime import datetime

def book_tracker(book, due_date, return_date, fine = 10):

    """Function to track book return and calculate fine if any.
    Returns:
        str: Fine or no fine message.
    """
    
    # Exception handling 
    try:
        due_date = datetime.strptime(due_date, '%d-%m-%Y') # Convert date to datetime object (strptime is strict so use correct format)
        return_date = datetime.strptime(return_date, '%d-%m-%Y')    
        
        # Check if return date before or  due date
        if return_date <=due_date:
            return f"{book} returned, No fine"     
        
        else:
            days_late = (return_date - due_date).days  # Calculate days late
            total_fine = days_late * fine # Calculate total fine
            return f"{book} returned, Fine: ₹{total_fine}"
    
    except Exception as e:
        return f"Error in Book Tracker: {e}"
    
# Main function to run book tracker
if __name__ == "__main__":

    # user input
    book_name = input("Book Name: ")
    due_date = input("Due Date (dd-mm-yy): ")
    return_date = input("Return Date (dd-mm-yy): ")

    # call bool_tracker function
    print(book_tracker(book_name, due_date, return_date))
