# nested 

#if nested
# a = 5
# b = 10
# c = 5

# if a > b:
#    print("A is greater.")
#    if a > c:
#       print('A is greaer than C as well')
#    elif a == c:
#       print("A and C are equal.")
#    else:
#       print("A is less than C.")
   
#    if b > c:
#       pass
# else:
#    print("B is greater.")
   
#    if b > c:
#       pass

# nested while
# a = 0

# while True:
#    print("Hello")
#    a += 1 #1, 3,5, 6
#    if a < 5:
#       print("A smaller than 5")
#       a += 1 #2, 4
#       continue
#    elif a == 5:
#       print("A is equal to 5")
#       a += 1
#       continue
#    print("End")
#    break

# print("Printed after the break ")

# # Task:
#    # ask user for their age
# age = int(input("Enter age:"))
#    # if user is 18 or older than 18, 
# if age>=18: 
#    # show that they can get the drivers license
#    print("You can get the driver's license")
#    # ask user if they have their their own vechile.
#    yn = input("Do you have your own vehicle?(y/n)")
#    # if yes print drive safe, if not print get a vechile.
#    if yn == "y":
#       print("Drive safe")
#    elif yn == "n":
#       print("Get a vehicle")
#    else:
#       print("Invalid input")
#    #if user is less than 18, show that they can't get the license yet.
# elif age < 18:
#    print("You cant get the driver license yet.")
# else:
#    print("Your input is invalid.")

#task:
# ask user for their name
# name = input("Enter the name:")
# # ask the number of times they want to display the name
# n = int(input("Enter the number of times you want to print the name:"))
# # print the name of user for that number of times
# # n = 3
# while True:
#    print(name)
#    n -= 1 # n =2,1,0
#    if n == 0:
#       break