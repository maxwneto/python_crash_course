# Simple If Statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# If-Else Statement
age = 18
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")

# If-Elif-Else Chain
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# More concise version of the above chain
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# Testing multiple conditions using `and`
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("Both are 21 or older.")
else:
    print("One or both are under 21.")

# Testing multiple conditions using `or`
if age_0 >= 21 or age_1 >= 21:
    print("At least one is 21 or older.")
else:
    print("Neither is 21 or older.")

# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'onions' in requested_toppings:
    print("Adding onions.")

# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Using Boolean Expressions
game_active = True
can_edit = False
if game_active:
    print("The game is currently active.")
if not can_edit:
    print("You do not have edit permissions.")
