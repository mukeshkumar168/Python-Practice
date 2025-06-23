import re

try:
    str1 = "Emma25 is Data scientist50 and AI Expert"

    words = str1.split() # remove the first and last spaces
    result = [] 

    # loops throught the words
    for word in words:
        if re.search(r'[A-Za-z]', word) and re.search(r'\d', word): # search word and number
            result.append(word)
       
    print("both letters and numbers:", result)

except Exception as e:
    print(f"Error: {e}")
