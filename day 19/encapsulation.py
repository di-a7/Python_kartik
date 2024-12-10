# encapsulation - wrapping attributes and method in a single unit, data hiding
# user '__' to define a private attribute or method
class Student:
   __email = None
   __password = None
   
   def get_email_and_password(self,email,password):
      self.__email = email
      self.__password = password
   
   def get_email(self):
      return self.__email

std1 = Student()
std1.get_email_and_password("student@gamil.com","password")
print(std1.get_email())
# print(std1.__email)