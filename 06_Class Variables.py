# Add a Class variable to Car that keeps track of the number of cars created.
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
    

class ElectricCar (Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

safari = Car("Tata","Safari")
# print(safari.fuel_type())
my_tesla = ElectricCar("Tesla","Model S","85kwh")
# print(my_tesla.get_brand())
# print(my_tesla.fuel_type())
print(Car.total_car)

