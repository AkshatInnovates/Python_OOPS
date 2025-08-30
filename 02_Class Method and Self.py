# Now we add a method to the car class that displays the full name of the car (Brand and model).
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fullName(self):
        return f"{self.brand} {self.model}"
    

my_car = Car('Inova','Crysta')

my_car2 = Car('Toyota','Corolla')
# print(my_car.brand)
# print(my_car.model)
# print(my_car2.brand)
# print(my_car2.model)

print(my_car.fullName())