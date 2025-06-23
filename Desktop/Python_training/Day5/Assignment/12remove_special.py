import re
def special_symbol(str):

    """Removes all the special characters """

    try:

        # Remove all special characters 
        result = re.sub(r'[^a-zA-Z0-9\s]', '', str)

        print("Modified String:", result)

    except Exception as e:
        print(f"Error: {e}")

s = '/*Jon is @developer & musician!!'
special_symbol(s)
