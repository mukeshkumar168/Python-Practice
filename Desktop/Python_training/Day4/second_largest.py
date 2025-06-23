def second_largest(numbers):

    """
    Function finds the second largest number in list
    Returns:
        int: second largest number"""

    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return "Only one number available"
    
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

# Example usage:
nums = [10, 20, 30, 40, 30, 20]
print("Second Largest:", second_largest(nums))
