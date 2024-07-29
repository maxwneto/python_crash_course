import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'pi.txt')

absolute_path = os.path.abspath(relative_path)

try:
    with open(absolute_path) as file_object:
        lines = file_object.readlines()

except FileNotFoundError:
    print("File not found or not exist!")

else:
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    
    birthday = input("Enter your birthday, in the for ddmmyy: ")
    if (birthday in pi_string):
        print("Your birthday appears in the first million of pi!")
    else:
        print("Your birthday does not appear in the first million of pi!")