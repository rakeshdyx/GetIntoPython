# person = {
#     "key" : "value",
#     "name" : "Rakesh",
#     "twitter" : "@rakeshdyx"
# }

# print(person)

# person['insta'] = "rakeshdmx"
# print(person)
# del person['key']
# print(person)

## ----------------booleans--------------------------

# can_code = True

# if can_code == True :
#     print("You can code")

##-------------------Type None------------------------

# wallet = None

# if wallet is None:
#     print("Nothing is in my wallet")

##-------------indexing and slicing---------------------

# lst = ['one', 'two','three', 'four','five']
# print(lst[2::])
# print(lst[-2::])

##--------------User Input---------------------------

# name=input("Type your name")

# age=input("Enter your age")

# print("Your age is :", name, "3 time of Your age is :", age * 3)

## ------------------type casting---------------------

# age = int(input("Enter your age :"))

# data_type = type(age)
# print(data_type)

# print("Your age in dougs age is", age * 2)

# grocery_list = ['Oats', 'Rice', 'Wheat', 'Oil', 'Rice']

## ----Task: Make a grocery list and type cast to tuple----

# print(type(grocery_list))

# grocery_list = tuple(grocery_list)

# print(grocery_list)

# print(type(grocery_list))

##-----------------formstting in python------------------

# name = "Rakesh"

# str_name = "Hello {}, how are you doing?".format(name)

# str_name = f"Hello {name}, how are you doing?"

# str_name = "Hello %s, how are you doing?" % name

# print(str_name)

##---------------comparision operator --------------------

# name = input("Enter your name :")

# if name == "Bob":
#     print(f"Welcome {name}!")
#     bring_food = "Pizza"
# elif name == "Rakesh":
#     print("Welcome to python pratice")
#     bring_food = "Tacos"
# else:
#     print("You are not Bob, get outta here")
#     bring_food = "Salmon"
# print(f"You are eating {bring_food}")'

# name = input("What is your name :")
# name = name.lower()

# if name != "bob":
#     print("You are not bob, get out from here")
# else:
#     print("Welcome to bobby boy")

##--------------comparision shortcuts -------------------

# comp_shortcuts = "Hello, Mr Divit"
# comp_shortcuts = None
# comp_shortcuts = ""
# comp_shortcuts = []

# if comp_shortcuts:
#     print("Varible has values")
# else:
#     print("No values assigned to the varibale")

##--------------Multiple comparision -------------------

# age = 31
# name = "Kelob"

# if age >= 18 and name == "Rakesh":
#     print("I can drink alcohol")
# else:
#     print("DONT DO ANYTHING")

# if age >= 18 or name == "Rakesh":
#     print("I can drink alcohol")
# else:
#     print("DONT DO ANYTHING")

##-------------For Loop-------------------------

# fav_food = ["Pizza", "Burger", "Tacos"]

# for food in fav_food:
#     if food == "Pizza":
#         size = input("What size of pizza you are looking for?")
#         print(f"You have ordered {size} pizza!")
#      print(f"My favorite food is: {food}")

# food = "Pizza!"

# for letters in food:
#     print(letters)

# focal = {
#     "name": "Rakesh",
#     "twitter": "@rakesh_dx",
#     "instagram": "rakeshdmx"
# }

# for key, value in focal.items():
#     print(f"Key is {key} and Value is {value} ")


# for key in focal.keys():
#     print(f"Key is {key}")

# for value in focal.values():
#     print(f"Value is {value}")

# for i in focal:
#     print(i) #default values you will get as keys

#--------------------While Loop------------------------

# x = 1

# while x <= 100:
#     print(x)
#     x=x+1

# items = ['One', 'Two', 'Three', 'Four', 'Five']

# for item in items:
#     if item == 'Two' or item == 'Four':
#         continue
#     print(item)

# for item in items:
#     if item == 'Three':
#         break
#     print(item)

# num = 0
# while num <=20:
#     num = num + 1
#     if num % 2 == 0:
#         continue
#     print(num)

# num = 0

# while num <= 10_00_000:
#     num = num + 1
#     if num == 13:
#         break
#     print(num)

#--------------Functions-----------------


# def somename(name, food="Pizza"):
#     if name.lower() == "rakesh":
#         print(f"Welcome {name}")

#     print(f"Hello {name}. Lets eat some {food}")

# somename("Rakesh", food='Sandwitch')

# def somename(name=None, food="Pizza"):

#     if name == None:
#         name = "Tolkin"
#     person_type = "Human"

#     if name == "Tolkin":
#         person_type = "God"
#     print(person_type)
#     print(f"Hello {name}. Lets eat some {food}")

# some_var = somename()

# print("The var is ", some_var) #by deafult the function value is None

# from nameScript import main


# def exp(num1, num2):
#     return num1 ** num2

# exp_num = exp(10, 2)
# print(exp_num)

#-------------Scope------------------
# name = "Tolkin"
# def scopping():
#     name = 'New'
#     return name

# print(scopping())

###=============Pratice 201 =======================###

#----------------IN Operator --------------

# body_part = input("Enter a boby part :").lower()

# rhym_body_parts = {"head", "solder", "knees", "toes" }

# if body_part in rhym_body_parts:
#     print("Entered body part is present in Rhym")
# else:
#     print("Choose a correct body part")


#--------------------NOT Operator ------------------------

# my_things = False

# if not my_things:
#     print("Things are false")

# name = "Kane Ezki"

# if name not in ["Rakesh", "Tolkin", "Kelob"]:
#     print(f"{name} is not in the club")

#------------------READING Files ---------------------

# with open('readme.txt', 'r') as file: #File is the context manager
#     print(file.read())
#     #By default python close the file here.

# with open('readme.txt', 'r') as file:
#     content = file.read()

# print("Reading from content file:", content)

#-------------------WRITING FILES-------------------------

# with open("writing_file.txt", "a") as file:
#     file.write("\nWriting to a file from the python code 2")
#     file.write("\n\tWriting to a file from the python code 3")

#--------------------READING MULTIPLE LINES--------------------

# with open('email.txt', 'r') as file:
#     emails = file.readlines()

# for email in emails:
#     # print(email.rstrip())
#     if 'hotmail' in email:
#         print(email.rstrip())


#------------------Writing a file and executing it--------------------
# filename = input("Enter the file name :")
# content = input("Input your content :")

# with open(filename, 'w') as file:
#     file.write(content)

# user_option = input("Do you want to read the content? y or n :")

# if user_option in ['y', 'n']:
#     if user_option == 'y':
#         with open(filename, 'r') as file:
#             print(file.read())

#-------------------FUNCTION inside of FUNCTION -----------------------

# def service1(stype):
#     print("Type of service1 is ", stype)
#     def service2():
#         print("Type of service2 is ", stype)
#     service2()
# service1("Premium")

#-----------------------Make a simple API ------------------------

# import requests

# req = requests.get("https://honeywell.edcast.com/")
# print(req.status_code)


# import requests
# import time

# while time:
#     req = requests.get("https://honeywell.edcast.com/")
#     print(req.status_code)

#     if req.status_code != 200:
#         #email to team
#         pass
#     time.sleep(10)

#-------------------Making a json API request --------------------
# import requests

# req = requests.get("https://swapi.dev/api/people/2/")
# person = req.json()

# print(f"Person name is \t\t\t {person['name']}")
# print(f"Person Birth year is \t\t {person['birth_year']}")

# print("Films involved are :")
# for film in person['films']:
#     film_req = requests.get(film)
#     film_names = film_req.json()
#     print(film_names['title'])

#----------------------Reading a JSON data -------------------------
# import json

# C3PO = '''{
# 	"name": "C-3PO",
# 	"height": "167",
# 	"mass": "75",
# 	"hair_color": "n/a",
# 	"skin_color": "gold",
# 	"eye_color": "yellow",
# 	"birth_year": "112BBY",
# 	"gender": "n/a",
# 	"homeworld": "https://swapi.dev/api/planets/1/",
# 	"films": [
# 		"https://swapi.dev/api/films/1/",
# 		"https://swapi.dev/api/films/2/",
# 		"https://swapi.dev/api/films/3/",
# 		"https://swapi.dev/api/films/4/",
# 		"https://swapi.dev/api/films/5/",
# 		"https://swapi.dev/api/films/6/"
# 	],
# 	"species": [
# 		"https://swapi.dev/api/species/2/"
# 	],
# 	"vehicles": [],
# 	"starships": [],
# 	"created": "2014-12-10T15:10:51.357000Z",
# 	"edited": "2014-12-20T21:17:50.309000Z",
# 	"url": "https://swapi.dev/api/people/2/"
# }'''

# C3PO = json.loads(C3PO)
# # print(C3PO['name'])
# # print(type(C3PO))

# C3PO['name'] = "Rakesh Swain"

# C3PO = json.dumps(C3PO)

# print(C3PO)


#---------------- Function *args ----------------------

# def startarg(*args):
#     total = 1

#     for num in args:
#         total = total * num
#     return total
# print(startarg(1, 2, 3, 4, 5))

#---------------- Function **kwargs ----------------------
# def person(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     if 'person_type' in kwargs:
#         print(f"Your are a {kwargs['person_type']} person")
#         print(f"Your age is ", kwargs.get("age"))



# person(name = "Rakesh", age = "32", person_type = "radiant")

# def order_pizza(name, addr, **toppings):
#     print(f"Ordered Person name is {name}")
#     print(f"Ordered person address is {addr}")
#     price = 18.00
#     for key, value in toppings.items():
#         price = price + 2
#     return price

# total_price = order_pizza("Rakesh", "India", jalapenos=True, extracheese=True, ham=True )
# print(total_price)

#------------------------ Mutable vs immutable -----------------------
#Refer web url - https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747

#-------------------------- List Enumeration -----------------------------


# animals = ["Cat", "Dog", "Pig", "Rhino", "Wolf"]

# for key, animal in enumerate(animals):
#     # print(f"{key +1}. \t {animal}")

#     if key % 2 == 0:
#         print(animal)

#------------------------- List Comprehension ----------------------

# number = [num**2 for num in [1, 2, 3 , 4, 5]]

# print(number)

# number = [num**2 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 == 0]
# number = [num**2 if num %2 == 0 else num**3 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
# print(number)

#--------------------------Dictionary Comprehensions----------------------

# fruit_price = [('orange', 25), ('apple', 30), ('kiwi', 45)]

# d = {}

# for key, value in fruit_price:
#     d[key] = value
# print(d)

# print(type(d))
