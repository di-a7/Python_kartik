# OOP ko concepts

# Inheritance
# Polymorphism
# Encapsulation
# Abstraction

# Inheritance - child class inherits the properties or attributes and methods of the parent class
class Car:
   brand = None
   color = None
   
   def set_car_data(self,brand,color):
      self.brand = brand
      self.color = color

class ElectricCar(Car):
   def speed(self,speed):
      self.speed = speed
   
   def set_car_data(self,brand,model):
      self.brand = brand
      self.model = model

car1 = Car() 
car1.set_car_data("Toyota","black")
# car1.speed("300 km/hr")
print(car1.brand)
print(car1.color)
print(car1.speed)

ecar1 = ElectricCar()
ecar1.set_car_data("Tata","tata model")
ecar1.speed("200 km/hr")
print(ecar1.brand)
print(ecar1.model)
print(ecar1.speed)