# Add a static method to the Car class that returns a general description of a Car.

class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand

    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or Disel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    

class ElectricCar (Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_car = Car("Tata","Safari")
# print(my_car.general_description())
print(Car.general_description())

