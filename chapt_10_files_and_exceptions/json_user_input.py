import json
import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'username.json')

absolute_path = os.path.abspath(relative_path)

try:
    with open(absolute_path) as file_object:
        username = json.load(file_object)

except FileNotFoundError:
    json.dump(username, file_object)
    print("We'll remember you when you come back, " + username + "!")

else:
    print("Welcome back, " + username + "!")