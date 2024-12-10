# OOP - Object Oriented Programming

# class - designs or blueprint, nature of the program
# object - instance of the class, data of created through class
# single class can have multiple objects

# constructor - method that is excuted when object is created
#self parameter takes the object name as argument

# class Student:
#    def __init__(self,first_name,last_name):
#       self.first_name = first_name
#       self.last_name = last_name
   
#    # def get_data(self, first_name, last_name):
#    #    self.first_name = first_name
#    #    self.last_name = last_name
   
#    def full_name(self):
#       return f"{self.first_name} {self.last_name}"
   
#    def __str__(self):
#       return f"This is the string representation of Student class."

# std1 = Student("john","doe")
# print(std1.full_name())

# std2 = Student("Diya","Stha")
# print(std2.full_name())



# std1.get_data("John", "Doe")
# print(std1)

# print(type('Hello'))

# print(std1.first_name)
# print(std1.last_name)
# print(std1.full_name())

# std2 = Student("Gopal","Shrestha")
# print(std2.first_name)
# print(std2.last_name)
# print(std2.full_name())

# a = 1
# print(type(a))


class Person:
   def __init__(self, name):
      self.name = name

person1 = Person("Ram")
print(person1.name)