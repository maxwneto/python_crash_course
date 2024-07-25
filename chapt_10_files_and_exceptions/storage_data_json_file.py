import json

file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/numbers.json'

numbers = [2, 3, 5, 7, 11, 13]
try:
    with open(file_path, 'w') as file_object:
         json.dump(numbers, file_object)

except FileNotFoundError:
    print("File not found or does not exist!")

else:
    # reading values from  JSON file
    with open(file_path, 'r') as file_object:
        loaded_numbers = json.load(file_object)
        print(loaded_numbers)
