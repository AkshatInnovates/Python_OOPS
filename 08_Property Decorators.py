# Use a property decorator in the Car class to make the model attribute read-only

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

my_car = Car("Tata","Safari")
# my_car,model = "city"

# print(my_car.general_description())
# print(Car.general_description())
print(my_car.model)


