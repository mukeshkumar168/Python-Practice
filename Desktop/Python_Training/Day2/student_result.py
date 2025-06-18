def student_result(name, mark):

    """ This function helps to determine the result of a student based on their marks.
    
    Returns:
        str: A message that the student has passed or failed.
    """

    try:

        # Check the mark above 35 mark 
        if mark >= pass_mark:
            return f'{name} has passed.'
        else:
            return f'{name} has failed.' 
        
    except Exception as e:
        return f"Error in finding result {e}"
    
# Main function to run the student result checker
if __name__ == "__main__":

    # user input
    student_name = input("Student Name: ")
    student_mark = int(input("Student Mark: "))
    pass_mark = int(input("Pass Mark: "))

    print(student_result(student_name, student_mark, pass_mark))

