class Employee:

    """ Employee Class
    Methods:
        display: Returns the Employee details
        role: Returns the Employee type
    """
    
    def __init__(self, name, salary):   #Constructor to initialize employee object
        self.name = name
        self.salary = salary

    # Returns the Employee's Name & salary
    def display(self):
        return f'Employee: {self.name}, Salary: Rs.{self.salary}'
    
    #  Returns the Role of Employee
    def role(self):
        return 'General Employee'
    
class Manager(Employee):    # inheriting from Employee

    """ Manager class inherited Employee class
    Methods:
        display: Returns the Manager details
        role: Returns the Manager type
        """

    def __init__(self, name, salary, department):   # constructor to initialize Manager object
        
        super().__init__(name, salary)     # call base class constructor
        self.department =  department

    # Method overriding
    def display(self):
        return f'Manager: {self.name}, salary: Rs.{self.salary}, Department: {self.department}'
    
    def role(self):
        return 'Manager'
    

# Polymorphism
def show_role(obj):
    """ 
        Function helps to display details based on the object
    """

    print(obj.display())
    print('Role: ', obj.role())
    print("--------------")

# Main Function
if __name__ =='__main__':

    emp1 = Employee("Arjun", 35000)
    mngr = Manager("Raj", 70000, 'Finanace')

    # calling Method in many forms
    show_role(emp1)
    show_role(mngr)