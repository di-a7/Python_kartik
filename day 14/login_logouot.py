#Requirment
# ask user if they want to login or register
# if register, ask for username and password and save it in a file
# if login, ask for username and password then check it in the file if the data of the user is in the file then print certain output if not print certain output
import json

def register():
   username = input("Enter the username:")
      
   password = input("Enter the password:")
   
   data = {username:password}
   print(data)
   f = open('user_data.txt','a')
   json_data = json.dumps(data)  #convert datas into json format
   f.write(json_data+"-")
   f.close()

def login():
   username = input("Enter username: ")
   password = input("Enter password: ")
   is_login = False
   f = open('user_data.txt','r')
   user_data = f.read().strip('-')
   list_user_date = user_data.split("-")
   f.close()
   # print(list_user_date)
   for i in list_user_date:
      if i != '':
         json_user_data = json.loads(i)  #converts json format into dictionary
         if username in json_user_data and json_user_data.get(username) == password:
            is_login = True

   if is_login == True:
      print('Login Success')
   elif is_login == False:
      print('Login Failed')


choose = input("login or signup (enter 'register' or 'login') : ").lower()

if choose == "register":
   register()
elif choose == "login":
   login()
