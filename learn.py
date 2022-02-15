# PYTHON FUNCTIONS PARAMETERS 
import math

def greet():
    print("Hello")
    print("Python is awesome")
    print("Everyone should learn python")

greet()

# function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Python is awesome {name}")
    print(f"Everyone should learn python {name}")

greet_with_name("Cute cat") #Python is awesome Cute cat  [and all other print statements]

# name is parameter and cute cat is the arguement
# parameter  is the name of the data that is suppose to come in there
# arguement is the actual piece of data that is being passed in

# functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
greet_with("Dennis", "Texas")#these are called positional arguements in python
# keyword arguements look like
greet_with(location = "Tenesse", name="Charlie Pride")

# coding challenge: paint area calculator: how many cans are we going to need in order to print a certain area

# 1 can can cover 5 square meters of the wall
# (height*width)/coverage
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
    # ceil() from the math module rounds up to the nearest whole number
    print(f"You will need {math.ceil((height*width)/cover)} cans of paint")

paint_calc(height=test_h, cover=coverage, width=test_w)

# coding exercise
# prime number checker
# also: prime numbe checker only cleanly divides itself and 1, any other number will have a remainder
n = int(input("Check this number: "))
def prime_checker(number):
    count = 0
    for num in range(1, n+1):
        if n % num == 0:
            count += 1
    if count == 2:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number")

prime_checker(number=n)
