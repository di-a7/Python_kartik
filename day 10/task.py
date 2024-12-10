# Task 
# create a list/tuple containing the name of people
name = ['ram','sita','hari','shyam','ritu']

# ask the user to enter a name
user = input("Enter your username: ")

# if the entered name is in the list then show "Login Successfully. Welcome and their name"
if user in name:
   print(f"Login Succesful. Welcome {user}")
else:
   print("Invalid username or password")
#    if user == i :
#       print(f"Login Success. Welcome {user}")
#       # break
# # if the entered name is not in the list then show "Invalid Credientials. their name not found"
#    else:
#       print(f"Invalid Credientials. {user} not found")
#       # break