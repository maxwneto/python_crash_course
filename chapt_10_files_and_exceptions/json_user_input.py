import json

file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/username.json'

try:
    with open(file_path) as file_object:
        username = json.load(file_object)

except FileNotFoundError:
    json.dump(username, file_object)
    print("We'll remember you when you come back, " + username + "!")

else:
    print("Welcome back, " + username + "!")