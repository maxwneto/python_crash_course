# create a variable and insert value of path file
file_path = '/home/max/Documents/projetos/python_crash_course/chapt_10_files_and_exceptions/files/hello.txt'

try:    
    # store hello.txt in file_object
    with open(file_path) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    print("File or directory does not exist!")

else:
    print(contents)