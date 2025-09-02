# Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance


class Car:
    total_car=0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.total_car+=1

    def get_brand(self):
        return self.__brand

    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or Disel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

    

class ElectricCar (Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S","85kwh")

class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "This is engine"
class ElectricCar2(Battery,Engine,Car):
    pass

my_newTesla = ElectricCar2("Tesla","Model S")
print(my_newTesla.engine_info())
print(my_newTesla.battery_info())




