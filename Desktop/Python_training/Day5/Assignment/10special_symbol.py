import re
def special_symbol(str):

    """ Replace all special Character with # 
    Returns:
        str: modified string"""

    try:

        # Replace all special characters with #
        result = re.sub(r'[^a-zA-Z0-9\s]', '#', str)

        print("Modified String:", result)

    except Exception as e:
        print(f"Error: {e}")

s = '/*Jon is @developer & musician!!'
special_symbol(s)
