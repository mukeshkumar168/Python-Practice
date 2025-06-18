# logic for converting celsius to fahernheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# logic for converting fahernheit to celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# main function to run the temperature convertor
def temperature_convertor():
    
    # user input for conversion choice and temperature
    print("Temperature Convertor")
    print("1. Celsius to Fahrenheit ", "2. Fahrenheit to Celsius", sep="|")
    choice = input("Choose an option (1 or 2): ")
    temperature = float(input("Enter the temperature: "))

    # choosing the conversion based on user input
    if choice == '1':
        print("Fahrenheit: ", celsius_to_fahrenheit(temperature))
    elif choice == '2':
        print("Celsius: ", fahrenheit_to_celsius(temperature))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    temperature_convertor()