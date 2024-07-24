# Reading an entire file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Reading line by line
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a list of lines from a file
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Writing to a file
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# Appending to a file
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

# Exception Handling
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# Using else block
try:
    answer = 5 / 1
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The answer is {answer}")

# Using finally block
try:
    print(5/1)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print("This will only run if no exception is raised.")
finally:
    print("This will run no matter what.")

# Storing data with JSON
import json

numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)
    print(numbers)
