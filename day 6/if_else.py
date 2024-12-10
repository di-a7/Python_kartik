# if else statement - multi lined statement
# when condition in the if statement is true then the statement inside the if block will be executed
# syntax : 
   # if (conditon):
   #     statement1
   # elif(condition):   "can be added according to the requirement"
   #     statement2
   # else:
   #  statement3
# a = 5
# b = 5

# if a > b:
#    print('A is greater than B.')
# elif a == b:
#    print('A is equal to B')
# else:
#    print('B is greater than A')


#Task:
# Requirements:
# ask user for 2 numbers
# ask user for the operation(+,-)
# if user enter + then add two number
# if user enter - then subtract two number
# else print invalid operation
# optional : you can use f string to print the output

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

op = input("Enter the operation (+,-): ")

if op == "+":
   add = a+b
   print(f"Sum: {add}")
elif op == "-":
   sub = a-b
   print(f"Substract: {sub}")
else:
   print("Invalid operation")

