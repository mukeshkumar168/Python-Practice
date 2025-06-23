
class Student:

    """ Student class 
    Methods:
        get_name(): get name from private variable
        set_name(): set name to private variable
        get_mark(): get mark from private variable
        set_mark(): set mark to private variable 
        display(): Display the Values

    """
    def __init__(self, name, mark):  # private variables
        self.__name = name 
        self.__mark = mark

    # Getter for name 
    def get_name(self):
        return self.__name 
    
    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for mark   
    def get_mark(self):
        return self.__mark

    # Setter for marks
    def set_mark(self, mark):

        try:
            if not 0<= mark <=100:
                raise ValueError("Mark should be less than 100")
            self.__mark = mark

        except Exception as e:
            print(f'Error in set_mark: {e}')
        
    # Display the Variables
    def display(self):
        print(f'Student: {self.__name}\nMarks: {self.__mark}')


# main function
if __name__ == "__main__":

    # Object for student
    s1 = Student("Rahul", 85)
    s1.display()

    # Updated marks
    s1.set_mark(95)
    print(f'updated mark: {s1.get_mark()}')

    # Updated name
    s1.set_name('Arjun')
    print(f'New Name: {s1.get_name()}')

    # Checking Exception Handling
    s1.set_mark(102)