import os

current_dir = os.path.dirname(__file__)

relative_path = os.path.join(current_dir, 'files', 'pi.txt')

absolute_path = os.path.abspath(relative_path)

try:
    with open(absolute_path) as file_object:
        lines = file_object.readlines()

except FileNotFoundError:
     print("File not found or does not exitst")

else:
     pi_string = ''
     for line in lines:
          pi_string += line.strip()

     print(pi_string[:52] + "...")
     print(len(pi_string))