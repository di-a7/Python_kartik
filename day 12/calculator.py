#Task:
# Requirements:
# ask user for 2 numbers
# ask user for the operation(+,-,*,/)
# if user enter + then add two number
# if user enter - then subtract two number
# if user enter * then multiply two number
# if user enter / then divide two number
# else print invalid operation
# optional : you can use f string to print the output
# ask user if they want to rerun the calculator if yes continue the loop and if no exit the loop
# handle the exceptions and print them out

while True:
   a = int(input("Enter 1st number: "))
   b = int(input("Enter 2nd number: "))

   op = input("Enter the operation (+,-,*,/): ")

   if op == "+":
      add = a+b
      print(f"Sum: {add}")
   elif op == "-":
      sub = a-b
      print(f"Substract: {sub}")
   elif op == "*":
      print(f"Multiplication:{a*b}")
   elif op == "/":
      print(f"Division: {a/b}")
   else:
      print("Invalid operation")
   
   user_choice = input("Do you want to continue? (yes/no):").lower()
   if user_choice != "yes":
      break