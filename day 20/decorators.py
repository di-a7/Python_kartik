# Decorators

# def Program(abc):
#    print("Welcome")
#    abc()

# @Program #(decorator) alternative(program(Hello)), Hello function is passed to the Program function
# def Hello():
#    print("Hello World")
#    print("Hello World")

# program(Hello)

# exersice
def swapping(fun):
      if a < b:
         a,b = b,a
      return fun(a,b)


@swapping
def div(a,b):
   print(a/b)

div1 = div(2,10)