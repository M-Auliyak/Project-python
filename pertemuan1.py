#  variabel
Site_salam ='halo '
site_name = 'Auly'
print(Site_salam +site_name)

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

#  display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))


num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


# print('New Year', 2023, 'See you soon!', sep= '- ')


a= 4
b= 8
hitung= a//b
print(hitung)
age = int(input("Enter your age: "))
citizen = input("U.S. citizen (yes/no)?: ")

# True only if (age >= 18) 
(citizen == "yes") is True
result = (age >= 18) and (citizen == "yes")
print(result)


age = int(input("Enter your age: "))

# Check if age is 18 or more
if age >= 18:
    print("Grant access to the website.")
else:
    print("you kids")

print("Program complete.")


# A list of three AI models
models = ["Fable", "ChatGPT", "Gemini"]

# Access items of the list one by one
for model in models:
    print(model)
    print("---")


# Iterate from i = 1 to i = 10
for i in range(1, 11):
    print(f"Displaying product {i}")


# for loop with else
stock = ['Laptop', 'Keyboard', 'Mouse']

order = input("Enter the product you want to buy: ")

for product in stock:
    if product == order:
        print(f"{order} is available. Adding to cart.")
        break
else:
    print(f"Sorry, {order} is out of stock.")

# identation
task = input("Task: ")

while task != "q":
    print("Task done!")
    task = input("Task: ")

# This statement is outside the loop
print("All tasks completed")


# While Loop with Else Clause example pin security
attempts = 3

while attempts > 0:
    pin = input("Enter PIN: ")

    if pin == "1212":
        print("Access granted.")
        break

    attempts -= 1
    print(f"Wrong PIN. {attempts} tries left.")
else:
    print("Account locked. Too many failed attempts.")


# break in loop
number = int(input("Enter a number: "))
for i in range(1, 6):

    # Terminate the loop if i equals number
    if i == number:
        break
    print(i)


# continu in loop
for i in range(1, 11):

    # Condition to check if a number is even
    if i % 2 == 0:
        continue
    print(i)


# creating list
cart = ["T-shirt", "Lamp", "Pen"]
print(cart)

# A list of mixed data types
my_list = [1, "Python", 3.14]
print(my_list)

# Empty list
my_list = []
print(my_list)


# creating tuple
# empty tuple
my_tuple = ()

# tuple having integers
my_tuple = (1, 2, 3)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# tuple can be created without parentheses
# also called tuple packing
my_tuple = 3, 4.6, "dog"
# tuple unpacking is also possible
a, b, c = my_tuple


# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)


# string method
text = "ChatGPT is great."

# Replace "ChatGPT" with "Claude"
new_text = text.replace("ChatGPT", "Claude")

print(new_text)


# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)

# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)


# update phyton set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

# using update() method
companies.update(tech_companies)

print(companies)


# Remove an Element from a Set
languages = {'Swift', 'Java', 'Python'}

print('Initial Set:',languages)

# remove 'Java' from a set
removedValue = languages.discard('Java')

print('Set after remove():', languages)


# union set
# first set
A = {1, 3, 5}

# second set
B = {0, 2, 4}

# perform union operation using |
print('Union using |:', A | B)

# perform union operation using union()
print('Union using union():', A.union(B)) 


# Set Intersection
# first set
A = {1, 3, 5}

# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)

# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B)) 


# difference set
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('Difference using &:', A - B)

# perform difference operation using difference()
print('Difference using difference():', A.difference(B)) 


# simmetric set
# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B)) 


# create dictionary
# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)


# Access Dictionary Items
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    
print(country_capitals["England"])


# Add Items to a Dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

print(country_capitals)


# remove dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)


# remove all
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# clear the dictionary
country_capitals.clear()

print(country_capitals)  


# change dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)


