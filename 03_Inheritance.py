# Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fullName(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar (Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85kwh")

print(my_tesla.model)
print(my_tesla.fullName())
# my_car = Car('Inova','Crysta')

# my_car2 = Car('Toyota','Corolla')
# print(my_car.brand)
# print(my_car.model)
# print(my_car2.brand)
# print(my_car2.model)

# print(my_car.fullName())