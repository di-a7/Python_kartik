# Function - same as variable but stores the block of statements in them
# we create function with the keyword def
# paranthesis whith function name is compulsory

# def helloWorld():
#    print("hello World 1.")
#    print("hello World 2.")
#    print("hello World 3.")
#    print("hello World 4.")
#    print("hello World 5.")

# helloWorld()

# print("Break")

# helloWorld()

# parameter - variable used when defining the function
# def person(name,age):
#    print(f"Name:{name}")
#    print(f"Age:{age}")

# name = "Ram"
# age = "30"

# # #argments - values passed to the function when it is called

# # positional argments - values passed according to the postion of corresponding parameter
# person("Ram","30")

# keyword argment
# def person(name,age,add,number):
#    print(name, age, add, number)

# person('ram',number = "9874563210",age = 12, add = "ktm")

# default argments:
a = 10
b = 40
def person(name = "Name1",age= 18,add = "Kathmandu",number= 98000000000):
   a = 12
   b = 15
   print(name, age, add, number)

person("Ram",20)

# Scope










# a = 12
# b = 13
# print(a)
# print(f"The sum {a} {a} {a}{a}")
# print("The sum",a, a, a,a)
# print(a,"and ",b,"Sumhek",a)