# ask user for login or register
# if register ask for their username, password and usertype(buyer/ seller),(format for data store may change) and store it in a file
# if login ask for their username, password and check if it exist in the file, if it exist print some message.
# if user is buyer then, show them the option to view products and to buy products and view bill, if the choice is view product then show them the details of the products
# if user is seller then, show them the option to add products and view products, if the choice is add products then they have to enter the name, description, price of the product


import json

def add_product(seller):
   name = input("Enter the name of product: ")
   description = input("Enter the description of the produce: ")
   price = input("Enter the price of the product: ")
   
   product = {"name":name, "description":description,"price":price,"seller":seller}
   f = open('C:/Users/ittra/OneDrive/Documents/Teach/kartik/product.txt','a')
   json_product = json.dumps(product)
   f.write(json_product+"-")
   f.close()

def view_product():
   f = open('C:/Users/ittra/OneDrive/Documents/Teach/kartik/product.txt','r')
   product = f.read().split("-")
   f.close()
   for i in product:
      print(i)

def view_your_product(seller):
   f = open('C:/Users/ittra/OneDrive/Documents/Teach/kartik/product.txt','r')
   product = f.read().split("-")
   f.close()
   for i in product:
      if i  != '':
         json_product = json.loads(i)
         if json_product.get("seller") == seller:
            print(json_product)

def register():
   username = input("Enter the username:")
   password = input("Enter the password:")
   usertype = input("Are you buyer or seller? ").lower()
   data = {
      "username":username,
      "password":password,
      "usertype":usertype
   }
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
   # print(list_user_date)
   f.close()
   for i in list_user_date:
      # {"username": "ram", "password": "ram", "usertype": "seller"}
      if i != '':
         json_user_data = json.loads(i)  # converts json format into dictionary

         if json_user_data.get('username') == username and json_user_data.get('password') == password:
            is_login = True
            usertype = json_user_data.get('usertype')

   if is_login == True:
      print("Login Success")
      if usertype == "seller":
         choice = input('''Enter
               1. Add product
               2. View your products
               >>''')
         if choice =="1":
            add_product(username)
         elif choice == "2":
            view_your_product(username)
            
      elif usertype == "buyer":
         choice = input('''Enter
               1. View product
               2. Buy product
               >>''')
         if choice == "1":
            view_product()
         elif choice == "2":
            pass
   elif is_login == False:
      print("Invalid credentials")

choose = input("login or signup (enter 'register' or 'login') : ").lower()

if choose == "register":
   register()
elif choose == "login":
   login()