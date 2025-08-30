#  Here, We create a car class with attributes like brand and model.Then create an instance of this class.
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car('Inova','Crysta')

my_car2 = Car('Toyota','Corolla')
print(my_car.brand)
print(my_car.model)
print(my_car2.brand)
print(my_car2.model)