import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'hello.txt')

absolute_path = os.path.abspath(relative_path)

try:
    with open(absolute_path) as file_object:
        lines = file_object.readlines()

except FileNotFoundError:
    print("File or directory not found.")

else:
    for line in lines:
        print(line.strip())
