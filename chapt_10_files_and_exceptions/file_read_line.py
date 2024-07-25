file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/hello.txt'

try:
    with open(file_path) as file_object:
       lines = file_object.readlines()

except FileNotFoundError:
    print("File or directory not found.")

else:
    for line in lines:
        print(line.strip())
