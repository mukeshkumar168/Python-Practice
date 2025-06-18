# Funtion to generate a salary slip for an employee
def generate_salary_slip(name, salary):

    # Calculate House Rent Allowance (HRA) 
    hra = salary * 0.20  

    # Calculate Dearness Allowance (DA)
    da = salary * 0.10   

    pf = 1800

    # Calculate total salary
    total_salary = (salary + hra + da) -pf



    # Print the salary slip
    print("--- Salary Slip ---")
    print("Name        :", name)
    print("Basic Salary: ", salary)
    print("HRA (20%)   : ", hra)
    print("DA (10%)    : ", da)
    print("Total Salary: Rs.", total_salary)


if __name__ == "__main__":

    # User input for employee details
    name = input("Enter employee name: ")
    salary = float(input("Enter basic salary: "))

    # Call the function to generate the salary slip
    generate_salary_slip(name, salary)
