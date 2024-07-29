import json

import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'hello.txt')

absolute_path = os.path.abspath(relative_path)

numbers = [2, 3, 5, 7, 11, 13]
try:
    with open(absolute_path, 'w') as file_object:
         json.dump(numbers, file_object)

except FileNotFoundError:
    print("File not found or does not exist!")

else:
    # reading values from  JSON file
    with open(absolute_path, 'r') as file_object:
        loaded_numbers = json.load(file_object)
        print(loaded_numbers)
