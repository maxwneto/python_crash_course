# hello_world.py
print("Hello, world!")


# Using Variables
message = "Hello, Python world!"
print(message)

# Changing Variable Values
message = "Hello, Python Crash Course world!"
print(message)


# Using Strings
name = "ada lovelace"
print(name.title())  # Output: Ada Lovelace

print(name.upper())  # Output: ADA LOVELACE
print(name.lower())  # Output: ada lovelace


# Combining (Concatenating) Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)  # Output: ada lovelace

# Using f-strings (Python 3.6+)
print(f"Hello, {full_name.title()}!")  # Output: Hello, Ada Lovelace!

# Using format() method (Python 3.5 and earlier)
print("Hello, {}!".format(full_name.title()))  # Output: Hello, Ada Lovelace!


# Adding Comments
# This is a comment
print("This code prints a message.")  # This comment is after a statement
