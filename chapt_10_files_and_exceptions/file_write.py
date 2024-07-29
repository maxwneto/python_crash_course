import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'programming.txt')

absolute_path = os.path.abspath(relative_path)

try:
    with open(absolute_path, 'w') as file_object:
        file_object.write("I love programming.\n")
        file_object.write("I love creating business apps.\n")
        file_object.write("I help my costumers improve theirs business.\n")

except FileNotFoundError:
    print("File not found or direct does not exist")

else:
    try:
        with open(absolute_path, 'r') as file_object:
            content = file_object.readlines()
            for line in content:
                print(line.strip())

    except FileNotFoundError:
        print("File not found when trying to read")