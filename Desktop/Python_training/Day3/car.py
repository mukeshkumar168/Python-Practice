class car:

    """Car Class
    Methods:
        __init__(brand, model, year): Initializes car object with brand, model, and year.
        __str__(): Returns  string representation of the car object.
    """
    def __init__(self, brand, model, year): # constructor to initialize car object

        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self): # print the object in  readable format

        return f"Brand: {self.brand} \nModel: {self.model}\nYear: {self.year}" 
    

if __name__ == "__main__":
    
    try:
        tata = car("Tata", "Nexon", 2022) # object for tata
        print(tata)

        suzuki = car("maruti", "swift", 2024) # object for volkswagen
        print(suzuki)

    except Exception as e:
        print(f"Error in Car: {e}")