#Parrot
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Greeter
name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#Using int() to Accept Numerical Input
age = input("How old are you? ")
age = int(age)
print(f"\nYou are {age} years old!")

#The Modulo Operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#Introducing while Loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

#Using a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city}!")

#Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Avoiding Infinite Loops
x = 1
while x <= 5:
    print(x)
    x += 1  # Make sure this line is not omitted to avoid an infinite loop