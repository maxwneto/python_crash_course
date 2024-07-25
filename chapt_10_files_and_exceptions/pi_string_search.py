file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/pi.txt'

try:
    with open(file_path) as file_object:
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