# A simple list of bicycle brands
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list
print(bicycles[0])  # Output: 'trek'
print(bicycles[0].title())  # Output: 'Trek'

print(bicycles[1])  # Output: 'cannondale'
print(bicycles[3])  # Output: 'specialized'

# Accessing the last element in a list
print(bicycles[-1])  # Output: 'specialized'

# Using individual values from a list
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding elements to a list
motorcycles.append('ducati')
print(motorcycles)

# Inserting elements into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing elements from a list
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove('yamaha')
print(motorcycles)

# Sorting a list permanently with the sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sorting a list temporarily with the sorted() function
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# Finding the length of a list
print(len(cars))

# Looping through a list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Making numerical lists
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# Using range() to make a list of numbers
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Using a loop to create a list of squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# List comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

print(players[:4])

print(players[2:])

print(players[-3:])

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)