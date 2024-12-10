# polymorphism

# a = 5
# b = 10
# print(a + b)

# x = "abc"
# y = "def"
# print(x + y )

class Dog:
   def move(self):
      return "Dog is walking."

class Bird:
   def move(self):
      return "Bird is flying."

class Fish:
   def move(self):
      return "Fish is swimming."

dog1 = Dog()
bird1 = Bird()
fish1 = Fish()

print(dog1.move())
print(bird1.move())
print(fish1.move())