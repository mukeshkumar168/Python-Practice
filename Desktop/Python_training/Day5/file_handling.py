class FileManager:
    """
    A custom context manager to handle opening and closing a file.
    methods:
        __enter__ => To oprn the file 
            Returns:  file
        __exit__ => To close and handle the error
        
    """

    def __init__(self, filename, mode):

        """ Stores filename, mode """
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):

        print("Opening file...")
        self.file = open(self.filename, self.mode)  # opens the file
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")
        
        self.file.close()   # closes the file
        # Exception handling
        if exc_type:
            print("Exception Type:", exc_type)
            print("Exception Value:", exc_val)
            print("Traceback:", exc_tb)
            return True 

# main function
if __name__ == "__main__":
    
    try:
        with FileManager("example.txt", "w") as f:
            f.write("Hello, this is written using a context manager!\n")
            # x = 1 / 0 
            print("Writing done.")

    except Exception as e:
        print("Error:", e)
