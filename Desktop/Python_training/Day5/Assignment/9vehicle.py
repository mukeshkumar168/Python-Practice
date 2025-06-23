import json

class Vehicle:

    """Vehicle Class:
    Methods:
        __init__ => Stores brand, year, model
        display_info => prints the values
        Returns:
            str: print the values"""

    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
    
    def display_info(self):
        return f"{self.brand} {self.model} {self.year}"
    
class Bus(Vehicle):

    """Bus Class
        Methods:
            __init: Stores brand, year, model, capacity
            display_info: Print the values"""
    
    def __init__(self, brand, year, model, capacity):
        super().__init__(brand, year, model)  # inherited by parent
        self.capacity = capacity
    
    def display_info(self):
        return f'{super().display_info()} capacity: {self.capacity}'
    
def vehicle_to_json(vehicle_obj):
    
    """Changing into json file"""

    try:
        
        return json.dumps(vehicle_obj.__dict__, indent = 4)  # changes into json string fotmat
    
    except Exception as e:
        print(f"Error converting to JSON: {e}")
        return None
    
#main funciton
if __name__ == "__main__":
    bus1 = Bus("Tata", 2022, "CityRide", 40)
    print("Bus Info:", bus1.display_info())

    vehicle_json = vehicle_to_json(bus1)
    print("\nJSON Output:")
    print(vehicle_json)