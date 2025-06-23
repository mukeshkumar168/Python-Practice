def fibonacci(n):

    """Generator to yield Fibonacci numbers up to n."""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Main Program
if __name__ == "__main__":
    try:

        # Take user input and ensure it's a valid positive number
        n = int(input("Generate up to: "))
        if n < 0:
            raise ValueError("Enter positive number.")

        print("Fibonacci sequence:")
        for num in fibonacci(n):  # To print the num
            print(num, end=' ')     
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    
    except Exception as e:
        print(f"Error in fibonacci function: {e}")
