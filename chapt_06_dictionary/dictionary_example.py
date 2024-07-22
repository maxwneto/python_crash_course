# Example: A simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])  # Output: green
print(alien_0['points'])  # Output: 5

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_1 = {}
alien_1['color'] = 'blue'
alien_1['points'] = 10
print(alien_1)

# Modifying values in a dictionary
alien_0['color'] = 'yellow'
print(alien_0['color'])  # Output: yellow

# Removing key-value pairs
del alien_0['points']
print(alien_0)

# Looping through all key-value pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping through all keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():
    print(name.title())

# Looping through all values
for language in favorite_languages.values():
    print(language.title())

# Nesting dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")