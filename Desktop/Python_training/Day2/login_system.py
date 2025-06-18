
def login_system():

    """Function to  login in the system
    Returns:
        str: Login success message or access denied message.
    """

    # Correct credentials
    crct_username = "admin"
    crct_password = "root"

    attempts = 3 # Number of attempts allowed

    # Loop until attempts over
    while attempts > 0:
        
        # if credentials are correct
        try:
            # user input 
            user_name = input('username: ')
            password = input('password: ')

            if ((user_name == crct_username) and (password == crct_password)):  # check credentials
                
                return 'Login Successful'
            
            else:
                attempts -= 1 # Decrease attempts if credentials are incorrect
                print(f'Invalid credentials. Attempt left: {attempts}')
            
        except Exception as e:

            print(f'Error in Login system: {e}')
        
    raise Exception(f"Access Denied {attempts}") # if all attempts are used up


# Main function to run the login system
if __name__ == '__main__':
    
    
    try:
        print(login_system())

    except Exception as e:
        print(e)


