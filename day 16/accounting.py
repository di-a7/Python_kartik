#Requirment
# ask user if they want to login or register
# if register, ask for username and password and save it in a file
# if login, ask for username and password then check it in the file if the data of the user is in the file then print certain output if not print certain output
# if user is valid user then ask his/her for three optioins:check balance, add balance
# check -print amount of user
# add  - ask amount they want to add, add the given amt with the entered amount and print the amount

# extra: if user balance xaina vaee, say them to add balance first
# Register() extra: check the file if the username is unique or not, if it is unique register the username if not then display that the username is already taken and to user another username

import json


def register():
   username = input("Enter the username:")
   
   password = input("Enter the password:")
   
   data = {username:password}
   
   print(data)
   
   f = open('user_data.txt','a')
   
   json_data = json.dumps(data)  #convert dictionary into json format
   
   f.write(json_data+"-")
   
   f.close()

def login():
   username = input("Enter username: ")
   password = input("Enter password: ")
   
   is_login = False
   
   f = open('user_data.txt','r')
   
   user_data = f.read().strip('-')
   
   list_user_date = user_data.split("-")   # seperate the strings from the given arguoment and convert them to list
   
   f.close()
   
   for i in list_user_date:
      
      if i != '':
         
         json_user_data = json.loads(i)  # converts json format into dictionary
         
         if username in json_user_data and json_user_data.get(username) == password:
            
            is_login = True

   if is_login == True:
      
      print('Login Success')
      
      choice = input("Enter \n 1. Check Balance \n2. Add Balance")
      
      if choice == '1':
         check_balance(username)
         
      elif choice == '2':
         add_balance(username)
      
   elif is_login == False:
      
      print('Login Failed')

def add_balance(username):
   
   amount = input("Enter the amount you want to add: ")
   
   dict_amount = {username:amount}
   
   f = open('C:/Users/ittra/OneDrive/Documents/Teach/kartik/accounting.txt','a')
   
   json_dict_amount = json.dumps(dict_amount)
   
   f.write(json_dict_amount+'-')
   
   f.close()
   
   print(f"Added {amount} to your account")

def check_balance(username):
   
   f = open('C:/Users/ittra/OneDrive/Documents/Teach/kartik/accounting.txt','r')
   
   total = 0
   
   user_data = f.read()
   
   list_user_data = user_data.split("-")
   
   for i in list_user_data:
      
      if i != '':
         
         dist_list_user_data = json.loads(i)
         
         if username in dist_list_user_data:
            
            amount = dist_list_user_data.get(username)
            
            int_amount = int(amount)
            
            total += int_amount
   print(total)
   f.read()

# check_balance('abc')

choose = input("login or signup (enter 'register' or 'login') : ").lower()

if choose == "register":
   register()
elif choose == "login":
   login()
