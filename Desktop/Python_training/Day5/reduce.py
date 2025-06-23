# import packages
from functools import reduce

def multiply_list(numbers):
    """ Using reduce to find the multiple
    Returns:
        int: Product"""

    try:   
        if not numbers:
            raise ValueError("List is empty.")
        
    
        product = reduce(lambda x, y: x * y, numbers)  # finding multiples using the reduce
        return f" product: {product}"

    
    except Exception as e:
        return f"Error: {e}"

# Example usage
numbers = [2, 5, 4]  
print(multiply_list(numbers))

