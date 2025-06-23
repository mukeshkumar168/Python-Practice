try:
    str1 = "apple"

    # Create an empty dictionary to store counts
    char_count = {}

    for char in str1:
        # Convert to lowercase to count 
        char = char.lower()

        # count if its repeated
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    print("Character Counts:")

    # loop to print the key and value
    for char, count in char_count.items():
        print(f"{char}: {count}")

except Exception as e:
    print(f"Error: {e}")
