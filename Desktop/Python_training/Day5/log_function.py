import time

# Decorator to log execution time
def log_execution_time(func):
    """
    A decorator that logs how long a function takes to execute.
    Returns:
        time
    """
    def wrapper(*args, **kwargs):
        print(f"Running '{func.__name__}'...")
        start_time = time.time()    # starting time 
        try:
            result = func(*args, **kwargs)   # Try running the actual function
            return result
        except Exception as e:
            print(f"error '{func.__name__}': {e}")

        finally:
            end_time = time.time()      # ending time 
            duration = end_time - start_time  # total time
            print(f"Finished '{func.__name__}' in {duration:.4f} seconds\n")
        
    return wrapper


# Another function with arguments
@log_execution_time
def multiply(a, b):
    time.sleep(1) # sleep for 1 second
    return a * b

@log_execution_time
def loop(n):
    for i in range(n):
        print(i)

# Run functions
if __name__ == "__main__":

    result = multiply(5, 7)
    print(f"Result : {result}")

    loop(100000)
