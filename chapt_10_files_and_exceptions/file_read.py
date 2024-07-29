import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'hello.txt')

absolute_path = os.path.abspath(relative_path)

try:   
    # store hello.txt in file_object
    with open(absolute_path) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print("File or directory does not exist!")

else:
    print(contents)