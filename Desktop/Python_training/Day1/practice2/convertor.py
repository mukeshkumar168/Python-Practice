#  Function to Convvert Currency
def currency_convertor():
    
    # User input for conversion choice and amount
    print("===Currency Convertor===")
    print("1. INR to USD ", " 2. INR to EUR", sep="|")

    choice = input("Choose an option (1 or 2): ")
    inr = float(input("Enter amount in INR: "))

    # Conversion logic based on user choice
    if choice == '1':
        usd = inr * 0.012  #  1 INR = 0.012 USD
        print("Amount in USD:", usd)

    elif choice == '2':
        eur = inr * 0.011 # 1 INR = 0.011 EUR
        print("Amount in EUR:", eur)

    else:
        print("Invalid choice") # If the user enters  other than 1 or 2 


# funtion to convert temperature
def temperature_convertor():

    # User input for conversion choice and temperature
    print("===Temperature Convertor===")
    print('1. Celsius to Fahrenheit', ' 2.Fahrenheit to celsius',sep = '|')

    choice = input("Choose an option(1 or 2 ): ")
    temperature = float(input('Enter the temperature: '))

    # Conversion logic based on user choice
    if choice == '1':
        fahrenheit = (temperature * 9/5) + 32  # fahrenheit = (Celsius * 9/5) + 32
        print('Fahrenheit: ', fahrenheit)

    elif choice == '2':
        celsius = (temperature - 32) * 5/9 # celsius = (Fahrenheit - 32) * 5/9
        print('Celsius: ', celsius)
    
    else:
        print("Invalid choice") # If the user enters  other than 1 or 2 


# Function to convert length
def length_convertor():
    
    # User input for conversion choice and length
    print('===length convertor===')
    print('1. Meter to kilometer ', ' 2. Kilometer to meter', sep='|')

    choice = input("Choose an option(1 or 2 ): ")
    length = float(input("Enter the length: "))

    # Conversion logic based on user choice
    if choice == '1':
        km = length / 1000  # kilometer = Meter / 1000
        print('Kilometer(km): ', km)

    elif choice == '2':
        m = length * 1000  # Meter = Kilometer * 1000
        print('Meter(m): ', m)
    else:
        print("Invalid choice")  # If the user enters other than 1 or 2


# Function to call the Convertor
if __name__ == "__main__":
    
    # Loop to keep the convertor running until the user chooses to exit
    while True:
        print("===Welcome to the Convertor===")
        print("1. Currency Convertor ", " 2. Temperature Convertor ", " 3. Length Convertor ", " 4. Exit", sep="|")
        choice = input("Choose an option (1-4): ")

        # Handling user choice
        if choice == '1':
            currency_convertor() # Call the currency convertor function
        elif choice == '2':
            temperature_convertor() # Call the temperature convertor function
        elif choice == '3':
            length_convertor()  # Call the length convertor function
        elif choice == '4':
            print("Exiting the Convertor. Goodbye!")  # Exit the loop and end the program
            break
        else:
            print("Invalid choice, please try again.")