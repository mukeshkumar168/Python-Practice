# Addition function
def add(x,y):
    return x + y

#Subraction function 
def subtract(x,y):
    return x-y

# Multiplication function   
def multiply(x,y):
    return x * y

# Division function    
def divide(x, y):
    if y == 0:
        return 'cannot divide by zero'
    else:
        return x/y

# Main function to run the calculator
if __name__ == '__main__':

    #Get user input
    num1 = int(input('Enter first number: '))
    num2  = int(input('Enter second number: '))
    operation = input('Enter operation (+, -, *, /): ')

    # Perform the operation based on user input
    if operation == '+':
        print('Result: ', add(num1, num2))
    elif operation == '-':
        print('Result: ', subtract(num1, num2))
    elif operation == '*':
        print('Result: ', multiply(num1, num2))
    elif operation == '/':
        print('Result: ', divide(num1, num2))
    else:
        print('Invalid operation')