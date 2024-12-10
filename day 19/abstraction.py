# Abstaction - hidding the unnessary details from the users

class Bike:
   def __init__(self):
      self.brake = False
      self.clutch = False
      self.acc = False
   
   def start(self):
      self.clutch = True
      self.acc = True
      return "Bike is started"

bike1 = Bike()
print(bike1.start())
