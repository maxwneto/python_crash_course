# working_with_list.py

# Creating a list
my_list = ["apple", "banana", "orange", "lemon"]

# Accessing list
print("First element:", my_list[0])

# Slicing a list
sublist = my_list[1:4]
print("Sliced list:", sublist)

# Appending a list
my_list.append("avocado")
print("After appending:", my_list)

# Inserting an element
my_list.insert(2, "watermelon")
print("After inserting:", my_list)

# Extending a list
my_list.extend(["grape", "mango", "pineapple"])
print("After extending:", my_list)

# Sorting a list
my_list.sort()
print("After sorting:", my_list)

# Sorting a list (without modifying the original list)
sorted_list = sorted(my_list)
print("Sorted list without modifying original:", sorted_list)

# Reversing a list
my_list.reverse()
print("After reversing:", my_list)

# Removing an element by value
my_list.remove("grape")
print("After removing 'grape':", my_list)

# Modifying an element by index
my_list[0] = "Cherry"
print("After modifying first element:", my_list)

# Deleting an element by index
del my_list[2]
print("After deleting element at index 2:", my_list)

# Deleting a slice of elements
del my_list[1:3]
print("After deleting slice from index 1 to 2:", my_list)

# Deleting entire list
del my_list
# Uncommenting the following line would raise an error as my_list is deleted
# print("After deleting entire list:", my_list)

# Recreate the list for further operations
my_list = ["apple", "banana", "orange", "lemon", "avocado", "watermelon", "grape", "mango", "pineapple"]

# Popping an element by index
element = my_list.pop(2)
print("Popped element:", element)
print("After popping element at index 2:", my_list)

# Finding an element's index
index = my_list.index("lemon")
print("Index of 'lemon':", index)

# Clearing a list
my_list.clear()
print("After clearing:", my_list)

# Recreate the list for further operations
my_list = ["apple", "banana", "orange", "lemon", "avocado", "watermelon", "grape", "mango", "pineapple"]

# Copying a list
new_list = my_list.copy()
print("Copied list:", new_list)

# Counting elements
count = my_list.count("apple")
print("Count of 'apple':", count)

# List comprehension
# Note: The original my_list does not contain numeric values, hence demonstrating with a numeric list
num_list = [1, 2, 3, 4, 5]
squares = [x**2 for x in num_list]
print("List of squares:", squares)

# Checking membership
is_present = "banana" in my_list
print("Is 'banana' present:", is_present)

# Minimum element
min_element = min(num_list)
print("Minimum element:", min_element)

# Maximum element
max_element = max(num_list)
print("Maximum element:", max_element)

# Sum of elements
total = sum(num_list)
print("Sum of elements:", total)

# Getting the list length
length = len(my_list)
print("Length of my_list:", length)

# Getting the last list index
last_index = len(my_list) - 1
print("Last index of my_list:", last_index)

# Printing all list elements using a for loop
print("All elements in my_list:")
for item in my_list:
    print(item)

# Creating a new numeric list using range function
numeric_list = list(range(10))
print("Numeric list using range:", numeric_list)
