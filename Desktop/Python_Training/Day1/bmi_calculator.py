# function to calculate BMI
def bmi_calculator(weight, height):
    
    # Convert height form centimeters to meters
    m_height = height / 100 
    print(f'height (m) {m_height}')
    print('the height in m{}'.format(m_height))

    # BMI formula weight(kg) / (height(m) ^ 2)
    bmi = weight/(m_height ** 2)

    # Print the BMI value
    print('your bmi is: ', bmi)

    # BMI category
    if bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi < 24.9:
        return 'Normal weight'
    elif 25 <= bmi < 29.9:
        return 'Overweight'
    else:
        return 'Obesity'
   
# Main function to run the BMI calculator
if __name__ == '__main__':

    # Exception handling for user input to ensure valid numbers
    try:
        weight = float(input('Enter your weight in kg:'))
        height = float(input('Enter your height in Centimeters:'))
        print(bmi_calculator(weight, height)) 

    # Handle invalid input
    except ValueError:
        print('please enter a valid')  